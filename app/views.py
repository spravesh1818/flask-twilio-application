import json
from flask import render_template, flash, jsonify, request
from twilio.rest import Client
from . import app, db
from .forms import SupportTicketForm
from .models import SupportTicket

from twilio.jwt.client import ClientCapabilityToken
from twilio.twiml.voice_response import VoiceResponse, Dial


@app.route('/')
def root():
    form = SupportTicketForm()
    return render_template('home.html', form=form)


@app.route('/tickets', methods=['GET', 'POST'])
def new_ticket():
    success_message = "Your ticket was submitted! An agent will call you soon."
    form = SupportTicketForm()

    if form.validate_on_submit():
        ticket = SupportTicket(**form.data)
        db.session.add(ticket)
        db.session.commit()
        flash(success_message)
    return render_template('home.html', form=form)


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('support_dashboard.html')


@app.route('/support/token', methods=['GET'])
def get_token():
    """Returns a Twilio Client token"""
    # Create a TwilioCapability object with our Twilio API credentials
    capability = ClientCapabilityToken(
        app.config['TWILIO_ACCOUNT_SID'],
        app.config['TWILIO_AUTH_TOKEN'])

    # Allow our users to make outgoing calls with Twilio Client
    capability.allow_client_outgoing(app.config['TWIML_APPLICATION_SID'])

    # If the user is on the support dashboard page, we allow them to accept
    # incoming calls to "support_agent"
    # (in a real app we would also require the user to be authenticated)
    if request.args.get('forPage') == '/dashboard':
        capability.allow_client_incoming('support_agent')
    else:
        # Otherwise we give them a name of "customer"
        capability.allow_client_incoming('customer')

    # Generate the capability token

    token = capability.to_jwt().decode('utf-8')

    return jsonify({'token': token})


@app.route('/support/call', methods=['POST'])
def call():
    """Returns TwiML instructions to Twilio's POST requests"""
    response = VoiceResponse()

    dial = Dial(callerId=app.config['TWILIO_NUMBER'])
    # If the browser sent a phoneNumber param, we know this request
    # is a support agent trying to call a customer's phone
    if 'phoneNumber' in request.form:
        dial.number(request.form['phoneNumber'])
    else:
        # Otherwise we assume this request is a customer trying
        # to contact support from the home page
        dial.client('support_agent')

    return str(response.append(dial))


@app.route('/sms',methods=['GET','POST'])
def sms():
    account_sid = 'AC32d46f59ea6199c04e52ea1800e79747'
    auth_token = '89ed211dcbfbded5d41ded5c9d4b11e4'

    my_phone_number = '+61480030084'
    client = Client(account_sid, auth_token)
    if request.method=='GET':
        messages = client.messages.list()
        return render_template('sms.html',messages=messages)

    if request.method=='POST':
        data=request.json
        phone_number=data['phonenumber']
        message_field=data['message']
        message = client.messages.create(
            body=message_field,
            from_=my_phone_number,
            to=phone_number
        )
        return {"msg": "Message sent successfully","sid":message.sid}


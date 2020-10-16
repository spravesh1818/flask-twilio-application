var message=$('#message_text');
var phone_number=$('#message_number');
var send_message_btn=$('#send_message_btn');
var sender=$('#message_sender');


function send_message(){
    send_message_btn.prop('disabled',true);
    data={'message':message.val(),'phonenumber':phone_number.val(),'sender':sender.val()};

    $.ajax({
      type: 'POST',
      url: "/sms",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(data),
      success: function(result){
        //message sent successfully and reload
          send_message_btn.prop('disabled',false);
          location.reload();
      }
    });



}

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .config import DevelopmentConfig

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
db=SQLAlchemy(app)

from . import views
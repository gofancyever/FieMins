from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object(config)
ma = Marshmallow(app)
db = SQLAlchemy(app)


from app import views
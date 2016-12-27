from app import db
from app import ma
from flask_marshmallow import fields
'''User Class'''

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)

    name = db.Column(db.String(80),index=True,unique=True)
    iconurl = db.Column(db.String(80), index=True, unique=True)
    accessToken = db.Column(db.String(80), index=True, unique=True)
    uid = db.Column(db.String(80), index=True, unique=True)
    appTokens = db.relationship('AppToken',backref = "appTokens",lazy = "dynamic")
    def __repr__(self):
        return '<User %r>' % self.name

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'iconurl')
user_schema = UserSchema()
users_schema = UserSchema(many=True)

'''AppToken Class'''

class AppToken(db.Model):
    __tablename__ = 'appTokens'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80),db.ForeignKey('users.accessToken'))
    accessToken = db.Column(db.String(80), index=True, unique=True)
    uid = db.Column(db.String(80), index=True, unique=True)
    expiration = db.Column(db.String(80), index=True, unique=True)
    openid = db.Column(db.String(80), index=True, unique=True)


    def __repr__(self):
        return '<User %r>' % self.accessToken

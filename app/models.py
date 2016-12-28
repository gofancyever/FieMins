from app import db
from app import ma
from flask_marshmallow import fields

'''AppToken Class'''
class AppToken(db.Model):
    __tablename__ = 'appTokens'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80),db.ForeignKey('users.uid'))
    user = db.relationship('User',backref = db.backref('appTokens',lazy = 'dynamic'))

    appType = db.Column(db.String(80), index=True, unique=False)
    accessToken = db.Column(db.String(80), index=True, unique=False)
    uid = db.Column(db.String(80), index=True, unique=False)
    expiration = db.Column(db.String(80), index=True, unique=False)
    openid = db.Column(db.String(80), index=True, unique=False)

    def __repr__(self):
        return '<AppToken %r>' % self.appType

class AppTokenSchema(ma.Schema):
    class Meta:
        fields = ('accessToken','expiration','openid','appType')
appToken_schema = AppTokenSchema()
appTokens_schema = AppTokenSchema(many=True)


'''User Class'''

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)

    name = db.Column(db.String(80),index=True,unique=False)
    iconurl = db.Column(db.String(80), index=True, unique=False)
    uid = db.Column(db.String(80), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % self.name

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'iconurl')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


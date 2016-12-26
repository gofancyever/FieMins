from app import db

'''User Class'''

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)

    name = db.Column(db.String(80),index=True,unique=True)
    iconurl = db.Column(db.String(80), index=True, unique=True)

    accessToken = db.Column(db.String(80), index=True, unique=True)
    uid = db.Column(db.String(80), index=True, unique=True)
    appTokens = db.relationship('AppToken',backref = "appTokens",lazy = "dynamic")

    def __init__(self,name,iconurl,uid):
        self.name = name
        self.iconurl = iconurl
        self.uid = uid

    def __repr__(self):
        return '<User %r>' % self.name


'''AppToken Class'''

class AppToken(db.Model):
    __tablename__ = 'appTokens'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80),db.ForeignKey('users.accessToken'))
    accessToken = db.Column(db.String(80), index=True, unique=True)
    uid = db.Column(db.String(80), index=True, unique=True)
    expiration = db.Column(db.String(80), index=True, unique=True)
    openid = db.Column(db.String(80), index=True, unique=True)

    def __init__(self,accessToke,uid,expiration,openid):
        self.accessToke = accessToke
        self.uid = uid
        self.expiration = expiration
        self.openid = openid

    def __repr__(self):
        return '<User %r>' % self.accessToken

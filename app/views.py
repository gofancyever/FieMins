
from app import app
from flask import request
from app import models
from app import db
import json
@app.route('/login',methods=['GET','POST'])
def login():
    uid = request.args.get('uid')
    if not request.args.get('uid') is None:
        return getUser(uid)
    else:
        return "200"



def getUser(uid):
    user = models.User.query.filter_by(uid='1').first()
    if not user is None:
        jsonStr = json.dumps(user, default=lambda obj: obj.__dict__)
        return json.dumps(user,default=lambda obj:obj.__dict__)
    else:
        return "404"

# def insertUser(dict):

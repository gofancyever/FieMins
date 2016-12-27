
from app import app
from flask import request,jsonify
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
    result = models.user_schema.dump(user)
    return jsonify(result.data)
    if not user is None:
        result = userSchema.dump(user)
        return jsonify(result.data)
    else:
        return "404"

# def insertUser(dict):

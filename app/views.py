
from app import app
from flask import request,jsonify
from app import models
from app import db

from app.error_extension import OEError
from app import models

''' Login '''
@app.route('/login',methods=['GET','POST'])
def login():
    uid = request.args.get('uid')
    if not request.args.get('uid') is None:
        try:
            userInfo = getUserInfo(uid)
            appTokens = getAppTokens(userInfo)
            userInfoDict = {"userInfo":models.user_schema.dump(userInfo).data}
            appTokensDict = {"appToken":models.appTokens_schema.dump(appTokens).data}
            return formatData([userInfoDict,appTokensDict],'200','success')
        except OEError as e:
            return formatData(None,e.code,e.msg)
    else:
        return formatData(None,300,'arg error')

'''register'''
@app.route('/register',methods=['GET','POST'])
def register():
    name = request.args.get('name')
    iconurl = request.args.get('iconurl')
    uid = request.args.get('uid')
    if verifyRegisterUser(name,uid):
        user = models.User(name=name,iconurl=iconurl,uid=uid)
        db.session.add(user)
        db.session.commit()
        return formatData(None, 200, 'success')
    else:
        return formatData(None,300,'arg error')


# register must value verify
def verifyRegisterUser(name,uid):
    return name != None and uid !=None


def getUserInfo(uid):
    user = models.User.query.filter_by(uid=uid).first()
    if not user is None:
        return user
    else:
        raise OEError(401,'user no found')

def getAppTokens(user):
    appTokens = user.appTokens.all()
    if not appTokens is None:
        return appTokens


def formatData(datas,code,msg):
    dictMerged = {
        "code":code,
        "msg":msg
    }
    try:
        for data in datas:
            dictMerged = dict(dictMerged, **data)
    except:
        pass
    finally:
        return jsonify(dictMerged)



from app import app
from flask import request,jsonify
from app import models
from app import db

from app.error_extension import OEError
from app import models

''' Login '''
@app.route('/login',methods=['GET','POST'])
def login():
    userID = request.args.get('userID')
    if not userID is None:
        try:
            userInfo = getUserInfo(userID)
            appTokens = getAppTokens(userInfo)
            userInfoDict = {"userInfo":models.user_schema.dump(userInfo).data}
            appTokensDict = {"appToken":models.appTokens_schema.dump(appTokens).data}
            return formatData([userInfoDict,appTokensDict],'200','success')
        except OEError as e: # no found user
            name = request.args.get('name')
            iconurl = request.args.get('iconurl')
            user = models.User(name = name,iconurl = iconurl,userID = userID)
            register(user)
            appTokens = getAppTokens(user)
            appTokensDict = {"appToken": models.appTokens_schema.dump(appTokens).data}
            userInfo = userInfo = getUserInfo(userID)
            userInfoDict = {"userInfo": models.user_schema.dump(userInfo).data}
            return formatData([userInfoDict, appTokensDict], '200', 'success')

    else:
        return formatData(None,300,'arg error')

@app.route('/addAppToken',methods=["GET",'POST'])
def addAppToken():
    userID = request.args.get('userID')
    app_type = request.args.get('appType')
    app_accessToken = request.args.get('accessToken')
    app_uid = request.args.get('uid')
    app_expiration = request.args.get('expiration')
    app_openid = request.args.get('openid')

    user = getUserInfo(userID)
    appToken = models.AppToken(appType = app_type,accessToken = app_accessToken,uid = app_uid,expiration = app_expiration,openid = app_openid)
    addAppToken(user = user,appToken = appToken)
    return formatData(None,200,'success')


def addAppToken(user,appToken):
    appToken.user = user
    db.session.add(appToken)
    db.session.commit()


def register(user):
    db.session.add(user)
    db.session.commit()


def getUserInfo(userID):
    user = models.User.query.filter_by(userID=userID).first()
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


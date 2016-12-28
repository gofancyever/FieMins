import json

class OEError(Exception):
    def __init__(self,code,msg):
        self.code  = code
        self.msg = msg
    def __str__(self):
        return repr(self.msg,self.code)


dictTest = {'user':{'a':1,'b':2}}


e = None


def error():
    raise OEError(200,'error')
try:
    a = error()
except OEError as e:
    print(e.code)



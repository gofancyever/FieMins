import json


class User():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

u = User('a',21,12)

d = dict(name='Bob', age=20, score=88)
print u.name

print json.dumps(u,default=lambda obj:obj.__dict__)
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
# print(json.dumps(s))
print(json.dumps(s, default=lambda d: d.__dict__))
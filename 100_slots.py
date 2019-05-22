

class Student(object):
	pass


s= Student()
s.name='Michael'	
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)	
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(33)	#no method
# print(s2.age)


class Student2(object):
	__slots__=('name', 'age')

s3 = Student2()
s3.name='Bob'
s3.score = 99	
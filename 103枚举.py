from enum import Enum, unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Sun
print(day1.value)	


@unique
class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):

	def __init__(self, name, gender):
		self.name = name
		self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')		
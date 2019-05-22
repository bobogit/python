# class Student(object):

# 	def __init__(self, name, socre):
# 		# 双下划线代表私有属性,.不建议这么写
# 		self.__name = name
# 		self.__score = score

# 	def print_score(self):
# 		print('%s, %s' % (self.__name, self.__score))


# bart = Student('Bart Simpson', 59)		
# print(bart.__name)


#############################work########################################
class Student2(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
    	return self.gender

    def set_gender(self, gender):
    	self.gender = gender
# 测试:
bart = Student2('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
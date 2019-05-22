def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax
	# return sum(args)

# print(calc_sum(1,2,3,4,5))	

def lazy_sum(*args):
	def sum():
		# return sum(args)
		ax = 0 
		for n in args:
			ax += n
		return ax
	return sum

f = lazy_sum(1,2,3,4,5)	

print('f()', f())

def createCounter():
	# s = [0]
	# def counter():
	# 	s[0]=s[0]+1
	# 	return s[0]
	# return counter;
	s = 0
	def counter():
		nonlocal s #设置为全局变量
		s+=1
		return s
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
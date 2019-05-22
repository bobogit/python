def power(x):
	return x * x

print('power=',power(5))
print('power=',power(15))

def power1(x, n=2):
	return x**n

print('power1=',power1(2, 10))	

def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

print('calc=', calc([1, 2,3]))

#可变参数
def calc1(*numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum

print('calc1', calc1(1, 3, 5, 7))	

l1 = [1, 2, 3]
l2 = (1, 2, 3)

#将数组或者tunple变成可变参数,在前面加入*
print('calc1-l1 = ', calc1(*l1))
print('calc1-l2 = ', calc1(*l2))

def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}
print('方法1')
person('Jack', 20, **extra)

#限制传入的参数, * 后面的表示限制参数
def person1(name, age, *, city, job):
	print(name, age, city, job)

print('限制参数')
person1('Jack', 24, city='Beijing', job='Engineer')	

#已经有命名关键字参数
def person2(name, age, *args, city, job):
	print(name, age, args, city, job)

print('命名关键字参数')	
args = [1,3,5,7,9]
person2('Tom', 24, *args, city='Shanghai', job='Boss')

#组合参数命名
def combo(a, b=0, *c, d, **e):
	print(a, b, c, d, e)

e={'e1':'e1', 'e2': 'e2'}

print('参数组合演示开始 -------------------------------------------------------------------------')

combo('可变参数A', '默认值参数B', '可变参数C1','可变参数C2', d='命名关键字参数d', **e)	

#接收1个或多个数,并计算乘积
def product(*list):
	if len(list) == 0:
		raise TypeError('参数列表不能为空')

	total = 1;
	for n in list:
		total *= n
	return total	

print(product(1,2,3,4,5))	

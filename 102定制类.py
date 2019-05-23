class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object(name:%s)' % self.name

print(Student("Michael"))		



class Fib(object):

	def __init__(self):
		self.a, self.b = 0,1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if(self.a > 10000):
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a+b
		return a		
			
for n in Fib():
	print(n)	

f = Fib()
print(f[5])			
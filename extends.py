class Animal(object):
	def run(self):
		print('Animal is running ...')

class Cat(Animal):
	def run(self):
		print('cat is running...')

	def eat(self):
		print('cat is eating')


class Dog(Animal):
	def run(self):
		print('dog is running...')

	def eat(self):
		print('dog is eating')

dog = Dog()
dog.run()


cat = Cat()
cat.run()
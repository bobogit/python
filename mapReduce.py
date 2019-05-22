def f(x):
	return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])	

print(list(r))

def normalize(name):
	def upper(n):
		return n[:1].upper()
	def lower(e):
		return e[1:].lower();
	return upper(name) + map(lower, name)		

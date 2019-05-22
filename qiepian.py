l1 = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#slice
print(l1[0:2])
print(l1[:2])

l2 = list(range(100))
print(l2)


#模拟trim方法
def trim(str):
	if str[:1] == ' ':
		print('if', str)
		return trim(str[1:])
	elif str[-1:] == ' ':
		print('elif',str)
		return trim(str[:-1]) 
	else:
		print('else')
		return str

print('trim===', trim('  hehe  '), 'len', len(trim('  hehe  ')))


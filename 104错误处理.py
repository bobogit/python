try:
	print('try ...')
	r = 10/2
	print('result', r)
except Exception as e:
	print('except', e)
finally:
	print('finally')

print('END')	
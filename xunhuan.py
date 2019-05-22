def findMinAndMax(l):
	if len(l) == 0:
		return (None, None)
	min = max = 0	
	for n in l:
		if min == 0 and max == 0:
			min = max = n
		elif n<min:
			min = n
		elif n>max:
			max = n

	return (min, max)			


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

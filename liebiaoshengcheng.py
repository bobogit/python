# -*- coding: utf-8 -*-

l = [x*x for x in range(1, 11)]
print(l)

l2 = [x*x for x in range(1, 11) if x % 2 == 0]
print(l2)

l3 = [m + n for m in 'ABC' for n in 'DEF']
print(l3)

import os
print([d for d in os.listdir('.')])

d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print(k,'=',v)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ x.lower() for x in L1 if isinstance(x, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
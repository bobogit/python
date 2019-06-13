import os
print(os.name)

# print(os.uname())     #windows下无效

print(os.environ.get('JAVA_HOME'))

print(os.path.abspath('.'))

print(os.path.join('d:/python', '111'))

# os.mkdir('e:/python/1/2/3')  #递归创建失败

print(os.path.split('d:/python/1/2/3/4.txt'))


print([x for x in os.listdir('.') if os.path.isdir(x)])


print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


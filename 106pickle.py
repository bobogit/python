import pickle
import json


d=dict(name='bob', age=20, score=88)
print(pickle.dumps(d))

f=open('./dump.txt', 'wb')        # wb  二进制方式写入
pickle.dump(d, f)
f.close()

f2 = open('./dump.txt', 'rb')
d2 = pickle.load(f2)
f2.close()
print(d2)

d3 = dict(name='Bob', age=20, score=80)
json.dumps(d3)

json_str='{"name": "bob", "age": 20, "score": 88}'
print(json.loads(json_str))

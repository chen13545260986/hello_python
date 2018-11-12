# 序列化模块
# 序列化--转向一个字符串数据类型
# 序列--字符串

# json:dumps序列化方法，loads反序列化方法
import json
dic = {'k1':'v1'}
str_d = json.dumps(dic)
print(type(str_d), str_d)
dic_d = json.loads(str_d)
print(type(dic_d), dic_d)

# json:dump和load
# f = open('fff', 'w', encoding='utf-8')
# json.dump(dic, f)
# f.close()

f2 = open('fff', 'r', encoding='utf-8')
res = json.load(f2)
print(type(res), res)
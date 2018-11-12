# 反射
# 内置函数：hasattr getattr delattr
# hasattr:返回bool值，判断对象内是否有该属性或方法
# getattr:返回类的属性值或方法


class School:
    dic = {'teachers':'show_teachers','studens':'show_students'}

    @staticmethod
    def show_teachers():
        print('this is teacher')

    @staticmethod
    def show_students():
        print('this is student')


print(hasattr(School,'dic'))
print(getattr(School,'dic'))
print(getattr(School,'show_teachers'))
res = getattr(School,'show_students')
res()
print('======')

for k in getattr(School,'dic'):
    print(k)

key = input('请选择：')
if hasattr(School,School.dic[key]):
    func = getattr(School,School.dic[key])
    func()
else:
    print('该选项不存在')
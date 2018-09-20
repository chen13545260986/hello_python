# 程序一旦发生错误，就从错误的位置停下来，不在继续执行后面的内容
# 使用try和except就可以处理异常
#   try是我们需要处理的代码
#   except后面跟一个错误类型，当代码发生错误就会执行里面的代码
#   except支持多分支
#   Exception万能异常,可以处理所有异常
#       单独异常处理应该写在万能异常前面
#   else:没有异常会执行的代码
#   finally:不管代码是否异常，都会执行
#       finally和return相遇时，依然会执行
#       通常用于函数里异常处理，不管是否异常，一般用于收尾处理

try:
    file = open('test.txt', 'r+')
    file.write('hello world')
except IOError:
    print('没有找到这个文件')
except Exception as e:
    print(e)
else:
    print('没有任何异常')
finally:
    print('执行完毕')
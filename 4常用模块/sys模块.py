# sys模块：和python解释器交互的模块
# 在模块中有一个__name__
# 当我们直接执行这个模块的时候，__name__ == ‘__main__’
# 当我们执行其他模块，在其他模块中引用了这个模块的时候，这个模块中的__name__ == ‘模块的名字’
# sys.moudles记录了所有被导入的模块
import sys

print(sys.platform)
print(sys.version)
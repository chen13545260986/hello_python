# 正则表达式：字符串匹配
# 用到re模块
import re

phone = input('请输入手机号：')
if re.match('^(13|15|16|17|18)[0-9]{9}',phone):
    print('手机号合法')
else:
    print('手机号不合法')
# coding=utf-8
# 由于注释和代码中有出现中文，开头要添加注释码 如上

# 1 hello world
print 'Hello,World.'

# 2 数据类型
print 45678+0x12fd2  # 123456
# 整数 十六进制整数
print 1.23e9  # 1230000000.0
print 1.23e-6  # 1.23e-06
# 浮点数科学计数法
print 'Learn Python in imooc'  # Learn Python in imooc
print "学习Python"  # "学习Python"
# 字符串 单引号、双引号都可以
print (100 < 99)  # False
print (0xff == 255)  # True
# 布尔值 True False 可以通过 and or not 运算
print ('none')  # none
print (None > 0)  # False
# 区分大小写

# 3 赋值
# 等差数列1 4 7 10 13 16 19 ...前 100 项的和。
x1 = 1
d = 3
n = 100
x100 = x1 + d*(n-1)
s = (x1 + x100)*n/2
print s  # 14950

# 4 字符串
s = '\tPython was started in \\1989 by \"Guido\".\t1\n\tPython is free and easy to learn.\t2'
print s  # Python was started in \1989 by "Guido".	1
#  Python is free and easy to learn.   2
# 常见转译内容 单引号 双引号 \n 表示换行 \t 表示一个制表符 \\ 表示 \ 字符本身

# 5 raw字符串和多行字符串
print ('\(~_~)/''\(~_~)/')  # \(~_~)/\(~_~)/
print ('\(~_~)/"\(~_~)/')  # \(~_~)/"\(~_~)/
print ('\\(~_~)/\\(~_~)/')  # \(~_~)/\(~_~)/
print (r'\(~_~)/''\(~_~)/'  # \(~_~)/\(~_~)/hhhhh
         "hhhhh")
print ('''\(~_~)/''\(~_~)/
    hhhhh''')  # \(~_~)/''\(~_~)/
#    hhhhh
# 使用r和'''

# 6 整数和浮点数运算
print (1 / 2)  # 0
print (1.0 / 2)  # 0.5
print (1 % 2)  # 1
print (1.0 + 10 / 4)  # 3.0
print ((1.0 + 10) / 4)  # 2.75
# 整数除为整数 带浮点出浮点 余数用%

# 7 布尔运算的短路计算
a = True
print a and 'T' or 'F'  # T
# a and b 如果 a 是 False，结果必定为 False，返回 a；如果 a 是 True，结果取决于 b，返回 b。
# a or b  如果 a 是 True，则结果必定为 True，返回 a；如果 a 是 False，结果取决于 b，返回 b。
# Python把 0 、 空字符串'' 和 None 是 False，其他数值和非空字符串是 True

# 8 创建list
L = ['Michael',True and False, 100 / 3]
E = []
print L,E  # ['Michael', False, 33] []
print (L,E)  # (['Michael', False, 33], [])
print L,'\n',E  # ['Michael', False, 33]
# []
print (L,'\n',E)  # (['Michael', False, 33], '\n', [])
# 在list中支持运算，使用print输出时，带括号的输出结果与不带括号的不同

# 9 按照索引访问list
L = ['Michael', 100 + 0.2, True and False, 100 / 3]
print L[0]  # Michael
print L[1]  # 100.2
print L[2]  # False
print L[3]  # 33
print L[-1]  # 33
print L[-4]  # Michael
# 负数可以逆序访问list

# 10 在list中添加新元素
M = ['Michael', 100 + 0.2, True and False, 100 / 3]
M.append(100 % 2)
print M  # ['Michael', 100.2, False, 33, 0]
# append将增加的内容添加到list的最后一位
M.insert(2, True + 2)
print M  # ['Michael', 100.2, 3, False, 33, 0]
# insert可以指定位置将增加的内容插入，在插入位置之后的元素自动后移

# 11 从list中取出指定位置的元素
N = ['Michael', 100 + 0.2, True and False, 100 / 3]
N.pop()  # 取出最后一个
print N  # ['Michael', 100.2, False]
N.pop(1)  # 取出指定位置
print N  # ['Michael', False]
N.pop(-1)  # 取出倒序位置
print N  # ['Michael']

# 12





















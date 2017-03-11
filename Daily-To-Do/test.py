# coding=utf-8

N = ['Michael', 100 + 0.2, True and False, 100 / 3]
N.pop()  # 删除最后一个
print N  # ['Michael', 100.2, False]
N.pop(1)  # 删除指定位置
print N  # ['Michael', False]
N.pop(-1)  # 删除倒序位置
print N  # ['Michael']
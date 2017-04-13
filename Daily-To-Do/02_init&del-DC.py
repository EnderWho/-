# coding=utf-8
# Filename : init&del-DC.py
# init初始化及del回收

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        print 'init %s' % self.name
        Person.population += 1

    def __del__(self):
        print 'del %s' % self.name
        Person.population -= 1
        print 'del %s' % Person.population

    def howMany(self):
        print 'howMany %s' % Person.population

x = 'a'
a = Person(x)
b = Person('b')
a.howMany()


'''
输出的内容：

# 调用 init 将 Person(x) 指给 a, population +1
init a
# 调用 init 将 Person('b') 指给 b, population +1
init b

# 调用 a.howMany
howMany 2

# 程序结束,回收资源，按调用的先后回收
del a
del 1
del b
del 0

'''
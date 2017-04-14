# coding=utf-8
# Filename: test.py

'''
我会建议你先解决这样一个问题：创建你自己的命令行 地址簿 程序。
在这个程序中，你可以添加、修改、删除和搜索你的联系人（朋友、家人和同事等等）以及它们的信息（诸如电子邮件地址和/或电话号码）。
这些详细信息应该被保存下来以便以后提取。



class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

  '''


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        Person.__init__(self, name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

class Teacher(Person):
    def __init__(self, name, gender):
        Person.__init__(self, name, gender)

# 在一个函数中，如果我们接收一个变量 x，则无论该 x 是 Person、Student还是 Teacher，都可以正确打印出结果：

def who_am_i(x):
    print x.whoAmI()

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female')

who_am_i(p)
who_am_i(s)
who_am_i(t)












# coding=utf-8
# Filename: open file and read print
# 创建文件并写入内容\对象,读取文件内容并以各种形式输出\输出对象

poem = '''\
Programming is fun

        use Python!
'''

# 新建文件,写入内容
addr = 'F:\\hello-world\\Daily-To-Do\\test-date\\03_w&p-file.txt'
f = open(addr, 'w')
f.write(poem)
f.close()


# 打开文件,逐行读取并输出
f = open(addr, 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print len(line), line,

# 逐行读取后,指针位于文件尾，用seek将指针移到文件头，输出当前指针位置
f.seek(0, 0)
print f.tell()

# 全文读取内容,并输出
f_all = f.read()
print f_all

# 通过readlines,将内容以list的形式存储在line中,并输出指定行数内容
f.seek(0, 0)
line = f.readlines()
print line[2]
f.close()


import cPickle
list_file = 'F:\\hello-world\\Daily-To-Do\\test-date\\03_w&p-file.data'

resource = ['apple', 'mango', 'carrot']

# 创建文件
f = file(list_file, 'w')
# 将对象写入文件中
cPickle.dump(resource, f)
f.close()

# 删除变量,并没有删除数据
'''
ex:
a = 1
b = a
del a
print b
b = 1
'''
del resource

# 读取对象
f = file(list_file)
resource_r = cPickle.load(f)
print resource_r
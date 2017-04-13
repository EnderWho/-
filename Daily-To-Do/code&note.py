#!/usr/bin/env python2
# coding=utf-8
# 由于注释和代码中有出现中文，开头要添加注释码 如上

# 数据类型
print 45678+0x12fd2  # 123456
# 整数 十六进制整数
print 1.23e9  # 1230000000.0
print 1.23e-6  # 1.23e-06
print ('none')  # none
print (None > 0)  # False
# 区分大小写

# 字符串
s = '\tPython was started in \\1989 by \"Guido\".\t1\n\tPython is free and easy to learn.\t2'
print s  # Python was started in \1989 by "Guido".	1
#  Python is free and easy to learn.   2
# 常见转译内容 单引号 双引号 \n 表示换行 \t 表示一个制表符 \\ 表示 \ 字符本身

# raw字符串和多行字符串
print ('\(~_~)/''\(~_~)/')  # \(~_~)/\(~_~)/
print ('\(~_~)/"\(~_~)/')  # \(~_~)/"\(~_~)/
print ('\\(~_~)/\\(~_~)/')  # \(~_~)/\(~_~)/
print (r'\(~_~)/''\(~_~)/'  # \(~_~)/\(~_~)/hhhhh
         "hhhhh")
print ('''\(~_~)/''\(~_~)/
    hhhhh''')  # \(~_~)/''\(~_~)/
#    hhhhh
# 使用r和'''

# 整数和浮点数运算
print (1 / 2)  # 0
print (1.0 / 2)  # 0.5
print (1 % 2)  # 1
print (1.0 + 10 / 4)  # 3.0
print ((1.0 + 10) / 4)  # 2.75
# 整数除为整数 带浮点出浮点 余数用%

# 布尔运算的短路计算
a = True
print a and 'T' or 'F'  # T
# a and b 如果 a 是 False，结果必定为 False，返回 a；如果 a 是 True，结果取决于 b，返回 b。
# a or b  如果 a 是 True，则结果必定为 True，返回 a；如果 a 是 False，结果取决于 b，返回 b。
# Python把 0 、 空字符串'' 和 None 是 False，其他数值和非空字符串是 True

# 创建list和tuple
L = ['Michael',True and False, 100 / 3]
E = []
print L,E  # ['Michael', False, 33] []
print (L,E)  # (['Michael', False, 33], [])
print L,'\n',E  # ['Michael', False, 33]
# []
print (L,'\n',E)  # (['Michael', False, 33], '\n', [])
# 在list中支持运算，使用print输出时，带括号的输出结果与不带括号的不同


T = ('Michael',True and False, 100 / 3)
# tuple除了不能修改组中的元素外，与list一致
T = (1,)  # 单元素的tuple加，让Python识别为tuple而不是整数
# 可以在list内插入tuple，tuple作为一整个元素输出
M = []
T = ('Michael',True and False, 100 / 3)
print T  # ('Michael', False, 33)
M.append(T)
M.append(1)
M.append('WER1')
print M[0]  # ('Michael', False, 33)
print M  # [('Michael', False, 33), 1, 'WER1']


# 可以在大list内插入小list，小list修改同步影响大list
M = []
T = ['Michael',True and False, 100 / 3]
print T  # ['Michael', False, 33]
M.append(T)
M.append(1)
M.append('WER1')
print M[0]  # ['Michael', False, 33]
print M  # [['Michael', False, 33], 1, 'WER1']
T.append(1)
print M  # [['Michael', False, 33, 1], 1, 'WER1']


# 可以修改tuple内的list
T = ('Michael',True and False, 100 / 3, [1, 'm', False])
print T  # ('Michael', False, 33, [1, 'm', False])
L = T[3]
L[1] = 'E'
print T  # ('Michael', False, 33, [1, 'E', False])


# 按照索引访问list
L = ['Michael', 100 + 0.2, True and False, 100 / 3]
print L[0]  # Michael
print L[1]  # 100.2
print L[2]  # False
print L[3]  # 33
print L[-1]  # 33
print L[-4]  # Michael
# 负数可以逆序访问list


# 在list中添加新元素
M = ['Michael', 100 + 0.2, True and False, 100 / 3]
M.append(100 % 2)
print M  # ['Michael', 100.2, False, 33, 0]
# append将增加的内容添加到list的最后一位
M.insert(2, True + 2)
print M  # ['Michael', 100.2, 3, False, 33, 0]
# insert可以指定位置将增加的内容插入，在插入位置之后的元素自动后移


# 从list中取出指定位置的元素
N = ['Michael', 100 + 0.2, True and False, 100 / 3]
N.pop()  # 取出最后一个
print N  # ['Michael', 100.2, False]
print N.pop()  # False
N.pop(1)  # 取出指定位置
print N  # ['Michael', False]
N.pop(-1)  # 取出倒序位置
print N  # ['Michael']

# 14 for 遍历list和tuple
# 取list中值的平均数
L = [75, 92, 59, 68]
s = 0.0
c = 0
for a in L:
    s = s + a
    c += 1  # 自增1 相当于 c = c + 1
print s / c  # 73.5

# 15 while和break 不符合判断条件后跳出
s = 0
x = 1
while True:
    s = s + x
    x += 2
    if x > 100:
        break
print s  # 2500

# 使用sys
import sys
print 'The command line arguments are:',

for i in sys.argv:
        print i


# 从zip文件解包
import zipfile
zfile = zipfile.ZipFile('archive.zip','r')
for filename in zfile.namelist():
    data = zfile.read(filename)
    file = open(filename, 'w+b')
    file.write(data)
    file.close()

'''
1.1 zipfile.ZipFile(fileName[, mode[, compression[, allowZip64]]])
mode,'r'表示打开一个存在的只读ZIP文件；'w'表示清空并打开一个只写的ZIP文件，或创建一个只写的ZIP文件；'a'表示打开一个ZIP文件，并添加内容。
compression表示压缩格式，可选的压缩格式只有2个：ZIP_STORE;ZIP_DEFLATED。ZIP_STORE是默认的，表示不压缩；ZIP_DEFLATED表示压缩。
allowZip64为True时，表示支持64位的压缩，一般而言，在所压缩的文件大于2G时，会用到这个选项；默认情况下，该值为False。

1.2 zipfile.close()
写入的任何文件在关闭之前不会真正写入磁盘。

1.3 zipfile.write(filename[, arcname[, compress_type]])
acrname是压缩文件中该文件的名字，默认情况下和filename一样
compress_type的存在是因为zip文件允许被压缩的文件可以有不同的压缩类型。

1.4 zipfile.extractall([path[, member[, password]]])
path解压缩目录，没什么可说的
member需要解压缩的文件名列表
password当zip文件有密码时需要该选项


2)高级应用
2.1 zipfile.is_zipfile(filename)
判断一个文件是不是压缩文件

2.2 ZipFile.namelist()
返回文件列表

2.3 ZipFile.open(name[, mode[, password]])
打开压缩文档中的某个文件

2.4 ZipFile.infolist()

2.5 ZipFile.getinfo(name)
上述文件返回ZipInfo对象，只不过一个返回的是列表，一个返回的是一个ZipInfo

ZipInfo类
2.6 ZipInfo.filename
2.7 ZipInfo.date_time
返回值的格式为(year,month,date,hour,minute,second)
2.8 ZipInfo.compress_type
2.9 ZipInfo.comment
2.10 ZipInfo.extra
2.11 ZipInfo.create_system
2.12 ZipInfo.extract_version
2.13 ZipInfo.reserved 总是0
2.14 ZipInfo.flag_bits
2.15 ZipInfo.volume
2.16 ZipInfo.internal_attr
2.17 ZipInfo.external_attr
2.18 ZipInfo.header_offset
2.19 ZipInfo.CRC
2.20 ZipInfo.file_size
2.21 ZipInfo.compress_size
2.22 ZipFile.testzip()
检查每个文件和它对应的CRC，如果有错误返回对应的文件列表

2.23 ZipFile.setpassword(password)
2.24 ZipFile.read(name[,password])
返回对应的文件
2.25 ZipFile.printdir()
打印压缩文件夹的信息
2.26 ZipFile.writestr(zipinfo_or_arcname, bytes)
PyZipFile类
zipfile.PyZipFile除了上面的方法和属性之外，还有一个特殊的方法
2.27 PyZipFile.writepy(pathname,basename)
一般情况下，仅仅压缩.pyc和.pyo文件，不压缩.py文件


创建目录在Python中可以使用os.mkdir()函数创建目录。其原型如下所示。
os.mkdir(path)

使用os.mkdir创建目录删除目录在Python os.rmdir()函数删除目录。其原型如下所示。
os.rmdir(path)

删除目录在Python中可以使用os.path.isdir()函数判断某一路径是否为目录。其函数原型如下所示。
os.path.isdir(path)


使用前 import os导入模块
os模块：
os.sep     可以取代操作系统特定的路径分割符
os.linesep  字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n' 而Mac使用'\r'。
os.name         字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
os.getcwd()   函数得到当前工作目录
os.getenv()和os.putenv()   函数分别用来读取和设置环境变量
os.listdir(dirname)： 列出dirname下的目录和文件
os.remove()  函数用来删除一个文件。
os.curdir:   返回但前目录（'.')
os.chdir(dirname): 改变工作目录到dirname
getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数
getmtime(path):文件或文件夹的最后修改时间
getctime(path):文件或文件夹的创建时间



os.path模块:
os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录,返回bool值
os.path.exists()函数用来检验给出的路径是否真地存在 返回bool
os.path.getsize(name):获得文件大小，如果name是目录返回0L 返回long 单位是字节
os.path.abspath(name):获得绝对路径
os.path.normpath(path):规范path字符串形式, 结果一般情况下把/变为//,
os.path.split(name):将name分割成路径名和文件名，结果为（路径名，文件名.文件扩展名）（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext(filename):分离文件名与扩展名 结果为（filename，扩展名） 如果参数为一个路径 则返回（路径，''）
os.path.join(path,name): 连接目录与文件名或目录 结果为path/name
os.path.basename(path):返回文件名 实际为把path的最后一个"/"分割，返回后者。不管参数是一个路径还是文件 与os.path.split(name)相同 不同之处后者返回两个值得元组
os.path.dirname(path): 返回文件路径 实际为把path的最后一个"/"分割，返回前者。不管参数是一个路径还是文件
os.system()函数用来运行shell命令



os模块包装了不同操作系统的通用接口，使用户在不同操作系统下，可以使用相同的函数接口，返回相同结构的结果。
os.name:返回当前操作系统名称（'posix', 'nt', 'os2', 'mac', 'ce' or 'riscos'）

os中定义了一组文件、路径在不同操作系统中的表现形式参数，如
os.sep（文件夹分隔符，windows中是 \ ）
os.extsep（扩展名分隔符，windows中是 . ）
os.pathsep（目录分隔符，windows中是 ; ）
os.linesep（换行分隔符，windows中是 \r\n ）

os中有大量文件、路径操作的相关函数，如：
listdir(path):列举目录下的所有文件
makedir(path):创建文件夹，注：创建已存在的文件夹将异常
makedirs(path):递归式的创建文件夹，注：创建已存在的文件夹将异常
remove(filename):删除一个文件
rmdir(path):删除一个文件夹，注：删除非空的文件夹将异常
removedirs(path):递归的删除文件夹，直到有一级的文件夹非空，注：文件夹路径不能以'\'结束
rename(src,dst):给文件或文件夹改名（可以改路径，但是不能覆盖目标文件）
renames(src,dst):递归式的给文件或文件名改名
walk(path):列举path下的所有文件、文件夹

os中与进程相关的操作，如：
execl(path):运行一个程序来替代当前进程，会阻塞式运行
_exit(n):退出程序
startfile(filename):用与文件关联的程序运行，关联程序打开后，立即返回
system(cmd):运行一个程序或命令，会立即返回，并在cmd执行完成后，会返回cmd退出代码
os.path:在不同的操作系统中调用不同的模块，是一个可import的模块，这个模块中提供很多有用的操作：
abspath(path):返回path的绝对路径，若path已经是绝对路径了，则保持。
basename(path):返回path中的文件名。
commonprefix(list):返回list中的统一前缀，用于获得一组字符串的左起相同的内容
dirname(path):返回path中的文件夹部分，结果不包含'\'
getsize(path):文件或文件夹的大小，若是文件夹返回0
isabs(path):返回是否是绝对路径
isfile(path):返回是否是文件路径
isdir(path):返回是否是文件夹路径
islink(path):返回是否是快捷方式
join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除
normcase(path):转换路径中的间隔符
normpath(path):转换路径为系统可识别的路径
realpath(path):转换路径为绝对路径
split(path):将路径分解为(文件夹,文件名)
splitext(path):将路径分解为(其余部分,.扩展名)，若文件名中没有扩展名，扩展名部分为空字符串
在操作与系统不支持的对象时，抛出OSError异常。




import datetime
import time

#string转datetime
>>>str = '2012-11-19'
>>>date_time = datetime.datetime.strptime(str,'%Y-%m-%d')
>>>date_time
datetime.datetime(2012,11,19,0,0)

#datetime转string
>>>date_time.strftime('%Y-%m-%d')
'2012-11-19'

#datetime转时间戳
>>>time_time = time.mktime(date_time.timetuple())
>>>time_time
1353254400.0

#时间戳转string
>>>time.strftime('%Y-%m-%d',time.localtime(time_time))
'2012-11-19'

#date转datetime
>>>date = datetime.date.today()
>>>date
>>>datetime.date(2012,11,19)
>>>datetime.datetime.strptime(str(date),'%Y-%m-%d')    #将date转换为str，在由str转换为datetime
>>>datetime.datetime(2012,11,19,0,0)


'''




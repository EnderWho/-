# coding=utf-8
# Filename: copy important file.py
# 将指定文件夹下的文件进行备份，在每次备份完成后，删除上一次备份的文件夹

import os, time, datetime
import zipfile

# 给定数据来源的文件夹
source = 'F:\\hello-world\\Daily-To-Do'

'''也可以通过玩家操作输入来获取文件夹地址

# 获得盘位置
file_name = raw_input('put a pan name!\n') + ':'
# 循环获得文件位置
while True:
    input_name = raw_input('put in a path!\n')
    # 通过输入空，来跳出循环
    if len(input_name) == 0:
        break
    # 如果输入目录存在，则继续，目录不存在则重新输入
    if os.path.exists(file_name + '\\' + input_name):
        file_name = file_name + '\\' + input_name
    else:
        print 'path error please reput!'

print file_name

同理 下文中备份文件夹地址也可通过输入获得，更进一步，可将上次输入的地址储存在指定的文件中，供下一次使用
'''

# 取出今日和昨日时间的字符串
Today = time.strftime('%Y%m%d')
Y = datetime.datetime.now() - datetime.timedelta(days=1)
Yesterday = Y.strftime('%Y%m%d')
print Yesterday

# 给定昨日和今日备份存储的文件夹
path_T = 'F:\\hello-world\\' + Today
path_Y = 'F:\\hello-world\\' + Yesterday
print path_Y

# 判断今天的文件夹是否存在
if os.path.exists(path_T):
    print "today done!"
else:
    # 不存在，则创建今日的文件夹
    os.mkdir(path_T)
    # 确定今日的压缩文件名
    cad = raw_input('put in a name!\n')
    if len(cad) == 0:
        command = time.strftime('%Y%m%d')
    else:
        command = time.strftime('%Y%m%d') + '_' + cad
    # 创建一个压缩文件
    zip_1 = zipfile.ZipFile(path_T + os.sep + command + '.zip', 'w', zipfile.ZIP_DEFLATED)
    # 遍历文件，获得文件地址并写入压缩文件
    for a, b, c in os.walk(source):
        for c1 in c:
            zip_1.write(os.path.join(a, c1))
    # 关闭压缩文件
    zip_1.close()

# 判断昨天的文件夹是否存在
if os.path.exists(path_Y):
    # 存在则删除文件夹及下面所有的文件，文件从下至上遍历
    for a1, b1, cs in os.walk(path_Y, topdown=False):
        # 遍历最下的文件，并删除
        for cc in cs:
            os.remove(os.path.join(a1, cc))
        # 遍历文件夹，删除
        for bb in b1:
            os.rmdir(os.path.join(a1, bb))
    os.rmdir(path_Y)
    print 'del copy_y'
else:
    print "yesterday doesn't copy"


'''
for a1, b1, cs in os.walk('F:\\hello-world\\1\\', topdown=False):
    for cc in cs:
        print (os.path.join(a1, cc))
    print 'end'
    for bb in b1:
        print (os.path.join(a1, bb))
    print 'over'

按照层级从上往下为：
@1 文件夹 1
@2 文件夹 21                          文件夹 22
@3 文件 31   文件夹 32                文件 33
@4

返回结果为：
# step 1 查最深的一层@4 中的内容(因为@3 内有文件夹，如无文件夹，则不会打开@4 层查询)
end
over

# step 2 查@3 中的文件及同级的文件夹
F:\hello-world\1\21\31.txt
end
F:\hello-world\1\21\32
over

# step 3 查@3 中另一个文件
F:\hello-world\1\22\33.txt
end
over

# step 4 查@2 中文件夹及文件
end
F:\hello-world\1\21
F:\hello-world\1\22
over


'''
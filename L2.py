# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
fo.write( "www.runoob.com!\nVery good site!\n");
# 关闭打开的文件
fo.close()


# 打开一个文件
foo = open("foo.txt", "r+")
str = foo.read(10);
print "读取的字符串是 : ", str

# 查找当前位置
position = foo.tell();
print "当前文件位置 : ", position
 
# 把指针再次重新定位到文件开头
position = foo.seek(0, 0);
str = foo.read(10);
print "重新读取字符串 : ", str
# 关闭打开的文件
foo.close()


import os
'''
# 重命名文件test1.txt到test2.txt。
os.rename( "test1.txt", "test2.txt" )

# 删除一个已经存在的文件test2.txt
os.remove("test2.txt")

# 创建目录test
os.mkdir("test")
'''

# 将当前目录改为"test"
os.chdir("test")
# 给出当前的目录
print os.getcwd()
# 删除”/test/newdir”目录
os.rmdir( "newdir"  )



f=open('w01.txt','rb+')
# e=f.tell()#只能读取当前偏移量
#必须以二进制方式打开文件时基准位置才能是1或者2
e=f.seek(3,2)#3:向后移动3个字节；
# #2:(默认值0,从头算起,1当前位置,2代表从文件末尾算起)
print(e)
f.write(b'vbnm')

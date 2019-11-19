#!usr/bin/python

'''
for x in range(5):
    for y in range(5):
        print(x,end="\t")
    print()    #起到换行的作用
    
'''



'''
#打印九九乘法表
for x in range(1,10):      #控制行数
    for y in range(1,x+1):    #控制乘法的第二个数，即乘法的每一行打印的乘法个数
        print("{0}*{1}={2}".format(x,y,(x*y)),end="\t")  #输出乘法表
    print()    #起到换行的作用
'''

'''
#使用列表和字典存储表格的数据
r1 = dict(name="高小一",age=18,salary=30000,city="北京")
r2 = dict(name="高小二",age=19,salary=20000,city="上海")
r3 = dict(name="高小三",age=20,salary=10000,city="深圳")
tb = [r1,r2,r3]   #将数据放入列表中列表

for x in tb:
    if x.get("salary")>10000:
        print(x)
'''



#打印乘法表，可以从命令行输入参数控制行数
import sys   #调用sys模块
z = sys.argv[1]   #从命令行输入参数控制循环行数
x = int(z)     #输入的数字为字符串类型，转换成int型
for m in range(1,x+1):  #通过带参数的方式输入来控制行数，从1到x,range函数用来创建整数列表
    for n in range(1,m+1):  #控制乘法的第二个数，即乘法的每一行打印的乘法个数,从1到m
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")  #输出乘法表
    print()    #起到换行的作用




'''
# 打印乘法表


z = input("请输入乘法表的行数：")    #通过输入行数控制循环次数
x=int(z)     #输入的数字为字符串类型，转换成int型
for m in range(1,x+1):   #将输入的数用来控制行数，从1到x,range函数用来创建整数列表
    for n in range(1,m+1):   #控制乘法的第二个数，即乘法的每一行打印的乘法个数,从1到m
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")  #输出乘法表
    print()    #起到换行的作用

'''




    







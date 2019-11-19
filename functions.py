
#定义函数


#将*打印10遍
def test01():
    print("*"*10)


test01()  #调用函数

#打印hello world
def test1():
    print("hello world")


test1()  #调用函数



#打印较大值
def printMax(a,b):
    '''打印较大值'''     #文档字符串又叫函数注释
    if a > b:
        print(a,"较大值")
    else:
        print(b,"较大值")

printMax(100,200)




#函数返回值
def add(a,b):
    print("计算两个函数的和：{0},{1},{2}".format(a,b,(a+b)))
    return a+b


c = add(10,20)
print(c)




#函数返回多个值
def test02(x,y,z):
    return [x*10,y*10,z*10]


d = test02(20,30,40)
print(d)





#全局变量和局部变量
a = 100
def test03():
    global a
    print(a)
    a = 300


test03()
print(a)



b = 50
def test04():
    b = 300
    print(b)


test04()
print(b)





#全局变量和局部变量效率比较
import math
import time
def test05():
    start = time.time()
    for i in range(1000000):
        math.sqrt(30)
    end = time.time()
    print("耗时{0}".format(end-start))




def test06():
    b = math.sqrt
    start = time.time()
    for i in range(1000000):
        b(30)
    end = time.time()
    print("耗时{0}".format(end-start))


test05()
test06()







#参数传递可变对象
a = [10,20]
def test07(m):
    print(m)
    m.append(30)


test07(a)
print(a)

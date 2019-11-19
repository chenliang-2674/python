#遍历元组
for x in (10,20,30):
    print(x*10)  #将元组中的数乘10打印出来
    
for y in "abcdef":
    print(y)  #依次打印字符

#遍历字典
d = {"name":"chenliang","age":18,"job":"student"}
for x in d:
    print(x)  #打印键对象
for x in d.keys():
    print(x)  #打印键对象
for x in d.values():
    print(x)  #打印值对象
for x in d.items():
    print(x)  #打印键对象和值对象


#计算1-100的累加和，奇数和，偶数和
sum_all = 0
sum_odd = 0  #奇数和
sum_even = 0  #偶数和
for x in range(101):
    sum_all += x
    if x%2 == 1:  #如果为奇数
        sum_odd += x
    else:
        sum_even += x  #如果为偶数
print("1-100累加总和:{0},奇数和:{1},偶数和:{2}".format(sum_all,sum_odd,sum_even))




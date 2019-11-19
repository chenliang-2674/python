'''
#测试break语句
while True:
    a=input("请输入一个字符(输入A结束)：")
    if a == "A":
        print("循环结束，退出")
        break
    else:
        print(a)
'''

'''
empNum = 0
salarySum = 0
salarys = []
while True:
    s = input("请输入员工的工资（输入A结束）:")
    
    if s.upper() =="A":
        print("输入完成，退出")
        break
    if float(s)<0:
        continue
    empNum +=1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数{0}".format(empNum))
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/empNum))

'''



for i in [1,2,3]:
    print(i)


#列表推导式
y = []
for x in range(1,50):
    if x%5==0:
        y.append(x*2)
print(y)





#字典推导式
my_test = "i love you,i love all,i love everything"
char_count = {c:my_test.count(c) for c in my_test}   #计算my_test中各个字符有多少个，并显示
print(char_count)



#集合推导式
b = {x for x in range(1,100) if x%8==0}
print(b)

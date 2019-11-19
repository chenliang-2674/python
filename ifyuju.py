'''
s=input("请输入一个数字：")
if int(s)<10:
    print("s是小于10的数字")
else:
    print("s是大于10的数字")


print("s是小于10的数字" if int(s)<10 else "s是大于10的数字")
'''


'''
score = int(input(" 请输入分数:"))
grade=""
if score<60:
    grade="不及格"
elif score<80:
    grade="及格"
elif score<90:
    grade="良好"
else:
    grade="优秀"
print("分数是{0},等级是{1}".format (score,grade))
'''



score = int(input("请输入一个在0-100之间的数字:"))
grade=""
if score>100 or score<0:
    score = int(input("输入错误！请重新输入一个在0-100之间的数字:"))
else:
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=70:
        grade="D"
    else:
        grade="E"
    print("分数是{0},等级是{1}".format (score,grade))
        

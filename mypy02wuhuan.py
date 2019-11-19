#绘制五环
#x=input("请输入环的半径：")
import turtle     #导入turtle模块
turtle.width(10)  #线的宽度
turtle.color("blue")  #环的颜色
turtle.circle(50) #环的半径

turtle.penup()         #把画笔抬起，不画
turtle.goto(120,0)     #笔移动到(120,0)的坐标位置
turtle.pendown()       #开始画
turtle.color("black")  #环的颜色
turtle.circle(50) #环的半径

turtle.penup()         #把画笔抬起，不画
turtle.goto(240,0)     #笔移动到(240,0)的坐标位置
turtle.pendown()       #开始画
turtle.color("red")  #环的颜色
turtle.circle(50) #环的半径

turtle.penup()         #把画笔抬起，不画
turtle.goto(60,-50)     #笔移动到(120,0)的坐标位置
turtle.pendown()       #开始画
turtle.color("yellow")  #环的颜色
turtle.circle(50) #环的半径

turtle.penup()         #把画笔抬起，不画
turtle.goto(180,-50)     #笔移动到(120,0)的坐标位置
turtle.pendown()       #开始画
turtle.color("green")  #环的颜色
turtle.circle(50) #环的半径



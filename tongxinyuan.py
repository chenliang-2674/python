'''
import turtle
t = turtle.Pen()

t.circle(10)

t.goto(0,-10)
t.circle(20)

t.goto(0,-20)
t.circle(30)

turtle.done() #程序执行，窗口仍然在
'''



#画同心圆

import turtle
t = turtle.Pen()

my_colors = ("red","orange","yellow","green","blue","purple")
t.width(5)
for x in range(10):
    t.penup()
    t.goto(0,-x*10)
    t.pendown()
    t.color(my_colors[x%len(my_colors)])  #设置画笔颜色
    t.circle(10+x*10)
    
turtle.done()

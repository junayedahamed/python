
import  turtle as t
#green rect

t.color("green")
t.begin_fill()
t.back(200)
t.forward(400)
t.left(90)
t.forward(180)
t.left(90)
t.forward(400)
t.left(90)
t.forward(180)
t.end_fill()
#red circle
t.color("red")
t.penup()
t.home()
t.begin_fill()
t.goto(-25,30)
t.pendown()
t.circle(60)
t.end_fill()
t.color("black")
t.penup()
t.home()
# bash

t.goto(-210,0)
t.right(90)
t.pendown()
t.forward(300)
t.right(90)
t.forward(15)
t.right(90)
t.forward(480)
t.right(90)
t.forward(15)
t.right(90)
for i in range(4):
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.back(10)
    t.right(90)
    t.forward(25)




t.forward(300)

t.left(55)
t.forward(30)
t.right(145)
t.forward(60.42)
t.right(140)



t.forward(28.80)
t.left(50)
t.penup()
t.forward(480)




t.done()
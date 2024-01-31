import turtle
import turtle as t

wn=turtle.screensize(900,900)
t.bgcolor("yellow")


for i in range (4):
    turtle.forward(100)
    turtle.right(90)
for j in range(4):
    turtle.back(100)
    turtle.right(90)

for i in range(3):
    turtle.forward(100)
    turtle.left(90)
turtle.home()
for i in range(3):
   if(i==1):
    turtle.right(90)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

turtle.done()
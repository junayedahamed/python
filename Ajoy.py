import  turtle as t

t.speed(18)
#green part
t.begin_fill()
t.color("green")
t.back(200)
t.forward(300)
t.left(90)
t.forward(150)
t.left(90)
t.forward(300)
t.left(90)
t.forward(150)
t.end_fill()
t.color("black")
# red circle


t.penup()
t.home()
t.goto(-80,25)
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
#  bash
t.color("black")
t.home()

t.back(230)
t.pendown()
t.right(90)
t.forward(300)
t.left(90)
t.forward(20)
t.left(90)
t.forward(330)
t.right(90)
t.forward(10)
t.back(10)
t.left(90)
t.forward(45)
t.right(90)
t.forward(10)
t.back(10)
t.left(90)

t.forward(45)
t.right(90)
t.forward(10)
t.back(10)
t.left(90)

t.forward(60)

t.left(90)
t.forward(20)
t.left(90)
t.forward(480)
#triangle

t.color("black")
t.begin_fill()

t.right(55)
t.forward(50)
t.back(50)
t.left(55+90)
t.forward(20)
t.right(90)
t.left(55)
t.forward(50)
t.right(55+90)
t.forward(101.91)
t.end_fill()









t.done()



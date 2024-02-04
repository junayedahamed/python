import  turtle as t


#head
t.circle(65)
#body
t.forward(200)
t.back(400)
t.right(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)
t.right(90)
#hand

t.forward(25)
t.right(90)
t.forward(200)
#hand circle
t.circle(11)
#last line right
t.back(10)
t.left(90)
t.forward(22)
t.right(90)
t.forward(10)
t.back(200)
# left  sholder fill
t.right(90)
t.forward(25)

# right hand
t.forward(450)
t.left(90)
t.forward(200)
# right hand circle
t.circle(-11)
t.back(10)
t.right(90)
t.forward(22)
t.left(90)
t.forward(10)

t.back(200)
t.left(90)
t.forward(22+225)
t.right(90)
for i in range(200//50):
    t.forward(50)
    t.circle(4)

t.left(90)
# right leg

t.forward(175)
t.right(90)
t.forward(125)
t.right(90)
t.forward(25)
#foot
t.left(90)
t.forward(35)
t.left(90)
t.forward(35)

t.left(135)
t.forward(49.49)
t.right(45)
t.left(90)
t.forward(7)
# right leg left arrow
t.right(90)
t.forward(125)

t.left(90)

# left leg

t.forward(175-32+175)
t.left(90)
t.forward(125)
# foot left leg

t.left(90)
t.forward(35)
t.back(27)
t.right(90)
t.forward(35)
t.left(90)
t.forward(35)
t.left(135)
t.forward(49.49)
t.left(45)
t.back(27)
# left leg right arrow
t.right(90)
t.forward(125)


#back to  center.................
t.right(90)
t.forward(155)
t.penup()
t.home()
# eye
#left eye
t.goto(-40,70)
t.pendown()
t.circle(8)
t.penup()
# right eye
t.forward(80)
t.pendown()
t.circle(8)
t.penup()
t.home()


# nose////////////

t.goto(0,55)
# t.right(90)
t.pendown()

t.back(15)
t.forward(30)
t.left(120)
t.forward(30)
t.left(120)
t.forward(30)
t.penup()
t.home()

# mouth

t.goto(0,35)
t.pendown()
t.back(25)
t.forward(50)
t.right(90)
t.forward(12)
t.right(90)
t.forward(50)
t.right(90)
t.forward(12)

# turtle going  home bye .......................

t.penup()
t.home()








t.done()
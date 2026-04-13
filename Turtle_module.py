# turtle moduel
import turtle
t=turtle.Turtle()
t.color("green","pink")
t.begin_fill()

for i in range(24):
    t.forward(40)
    t.left(90)
t.right(23)
t.left(78)
t.forward(90)
t.left(190)
t.forward(720)

t.end_fill()

turtle.done()

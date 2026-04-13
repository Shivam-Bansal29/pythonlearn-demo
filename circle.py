import turtle
t=turtle.Turtle()
t.speed(0)
t.colors=['orange','white']
t.hideturtle()
for i in  range(122):
    t.goto(0,0)
    t.color(t.colors[i%2])
    t.forward(130)
    t.left(3)
    t.circle(40)
    t.forward(130)
    t.right(180)
turtle.done()

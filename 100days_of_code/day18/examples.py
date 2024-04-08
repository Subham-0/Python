import turtle as t 
tim = t.Turtle()
k = 10
for i in range(0,4):
    for i in range(1,10):
        tim.forward(k)
        tim.penup()
        tim.forward(k)
        tim.pendown()
    tim.left(90)

s = t.Screen()
s.exitonclick()


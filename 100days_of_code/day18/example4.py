# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)
# tim.speed(0)
# tim.pensize(1)
# for a in range(360):
#     tim.color(random_color())
#     tim.circle(80)
#     tim.setheading(a*8)
#     tim.forward(5)

# sc = t.Screen()
# sc.exitonclick()

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
tim.speed(0)


def draw_spirograph(size_of_gap):
    for a in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(80)
        tim.setheading(tim.heading()+size_of_gap)
        
draw_spirograph(6)

sc = t.Screen()
sc.exitonclick()

# from turtle import Turtle,Screen

# import turtle
# t = turtle.Turtle()

import turtle as t
import heroes as h

print(h.gen())

t.shape(name="turtle")
# t.shape(name="circle")
# t.shape(name="square")
# t.shape(name="triangle")
# t.shape(name="arrow")

t.color("red")
t.color("LemonChiffon4")
# https://cs111.wellesley.edu/reference/colors


#drawing square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.left(90)
t.forward(100)
t.left(90)


screen = t.Screen()
screen.exitonclick()
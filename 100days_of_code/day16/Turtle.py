# import turtle
# timmy = turtle.turtles() #constructing turtle object

# or 

from turtle import Turtle,Screen       #one of the other class inside the turtle module
timmy = Turtle()
print(timmy)                            #its a object that being printed
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(76.8)

screen = Screen()
height = screen.canvheight
print(height)
screen.exitonclick()


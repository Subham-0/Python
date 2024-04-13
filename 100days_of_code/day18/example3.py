import turtle as t 
import random 
 
tim = t.Turtle()
t.colormode(255)

# colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return (r,g,b)

direction = [0,90,180,270]
tim.speed(0)
tim.pensize(15)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
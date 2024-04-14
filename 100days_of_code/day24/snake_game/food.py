from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed(1)
        
    def refresh(self):
        self.goto(random.randint(a=-280,b=280),random.randint(a=-280,b=280)) 
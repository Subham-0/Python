import random
from turtle import Turtle,Screen

screen = Screen()
is_race_on =False
screen.setup(width=600,height=600)
user_choise = screen.textinput(title="Make your bet" , prompt="Which turtle will win the race? Enter a color ")
colors = ["red","orange","yellow","green","blue","purple"]
y_position =[-90,-40,10,60,110,160]
all_turtle = []


for turtle_index in range(0,6):
    kachhua = Turtle(shape="turtle")
    kachhua.color(colors[turtle_index])
    kachhua.penup()
    kachhua.goto(x=-290,y=y_position[turtle_index])
    all_turtle.append(kachhua)
    
if user_choise:
    is_race_on =True   

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>295:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choise:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    

screen.exitonclick()
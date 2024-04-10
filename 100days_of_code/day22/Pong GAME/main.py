from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scorebd = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detecting collision with the wall
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.y_bounce()

    #Detecting collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.x_bounce()
        
        
    #Detecting R paddle misses
    if ball.xcor() > 380 :
        ball.reset_position() 
        scorebd.l_point()
        
    #Detecting y paddle misses
    if ball.xcor() < -380 :
        ball.reset_position() 
        scorebd.r_point()

        

screen.exitonclick()


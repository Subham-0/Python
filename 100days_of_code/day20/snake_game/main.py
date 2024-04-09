
import time
from turtle import Turtle,Screen
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)

# timmy1 = Turtle()
# timmy1.color('white')
# timmy1.shape('square')

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up") 
screen.onkey(snake.down,"Down") 
screen.onkey(snake.right,"Right") 
screen.onkey(snake.left,"Left") 

    
game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
        


screen.exitonclick()
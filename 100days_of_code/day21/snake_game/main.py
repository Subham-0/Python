
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboad import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)

# timmy1 = Turtle()
# timmy1.color('white')
# timmy1.shape('square')

snake = Snake()
food = Food()
score = Scoreboard()

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
    
    #Detect collision with the food 
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    #Detect collision with the wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.game_over()
        game_is_on = False
        
    #Detect colliction with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
        
    


screen.exitonclick()
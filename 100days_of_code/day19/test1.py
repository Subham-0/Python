from turtle import Turtle , Screen

tiny = Turtle()
screen = Screen()


def move_forward():
    tiny.forward(10)

def move_backward():
    tiny.backward(10)

def turn_left():
    tiny.left(10)

def turn_right():
    tiny.right(10)
    
def clear():
    tiny.clear()
    tiny.reset()

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear,"c")
screen.exitonclick()

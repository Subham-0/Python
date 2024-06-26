from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",15,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0,y=270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} HighScore = {self.high_score}",align=ALIGNMENT,font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.clear()
    #     self.goto(0,-50)
    #     self.write(f"GAME OVER \n \n    score {self.score}",align=ALIGNMENT,font=FONT)
       
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
        
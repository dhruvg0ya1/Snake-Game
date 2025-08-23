from turtle import Turtle
FONT = ('Comic Sans MS', 10 , 'normal')
GAME_OVER_FONT = ('Elephant', 25, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("hs.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.write(f'Score: {self.score}', False, 'center', FONT)
    
    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, 'center', FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("hs.txt", mode = 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, 'center', FONT)
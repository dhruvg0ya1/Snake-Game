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
        self.color('white')
        self.write(f'Score: {self.score}', False, 'center', FONT)
    
    def inc_score(self):
        self.score += 1
        self.write(f'Score: {self.score}', False, 'center', FONT)
                   
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', False, 'center', GAME_OVER_FONT)
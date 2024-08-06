from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color('red')
        self.speed('fastest')
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.rand_loc()
        
    def rand_loc(self):
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.goto(rand_x, rand_y)
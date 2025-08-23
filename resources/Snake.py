from turtle import Turtle, Screen

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
        
    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_part(i)
            
    def add_part(self, i):
        new_part = Turtle('square')
        new_part.color('cyan')
        new_part.penup()
        new_part.goto(i)
        self.parts.append(new_part)
        
    def extend(self):
        self.add_part(self.parts[-1].position())
            
    def move(self):
        for i in range(len(self.parts)-1, 0, -1):
            new_x = self.parts[i -1].xcor()
            new_y = self.parts[i -1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def reset(self):
        for i in self.parts:
           i.goto(6969, 6969) 
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]
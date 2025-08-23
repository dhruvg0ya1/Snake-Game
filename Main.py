from resources.Snake import Snake, Screen
from resources.Food import Food
from resources.Scoreboard import Scoreboard
import time
import pygame

pygame.mixer.init()
eat_sound = pygame.mixer.Sound('Snake-Game/resources/eating.wav')
hit_sound = pygame.mixer.Sound('Snake-Game/resources/hit.wav')

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        eat_sound.play()
        food.rand_loc()
        score.clear()
        score.inc_score()
        snake.extend()
        
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        hit_sound.play()
        Scoreboard.reset()
        snake.reset()

    for i in snake.parts[1:]:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 1:
            Scoreboard.reset()
            snake.reset()

screen.exitonclick()
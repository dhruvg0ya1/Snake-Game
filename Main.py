from components.Snake import Snake, Screen
from components.Food import Food
from components.Scoreboard import Scoreboard
import time
import pygame

pygame.mixer.init()
music = pygame.mixer.Sound('sounds/music.wav')
music.play(-1)
eat_sound = pygame.mixer.Sound('sounds/eating.wav')
hit_sound = pygame.mixer.Sound('sounds/hit.wav')

screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

paused = False
def toggle_pause():
    global paused
    paused = not paused

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')
screen.onkey(toggle_pause, 'space')

game_on = True
speed = 0.1

while game_on:
    screen.update()
    if not paused:
        time.sleep(speed)
        snake.move()
        if snake.head.distance(food) < 15:
            eat_sound.play()
            food.refresh()
            score.clear()
            score.inc_score()
            snake.extend()
            speed = max(0.03, speed - 0.005)
        if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
            game_on = False
            music.stop()
            hit_sound.play()
            score.reset()
            snake.reset()
            score.game_over()
        for i in snake.parts[1:]:
            if snake.head.distance(i) < 1:
                game_on = False
                music.stop()
                hit_sound.play()
                score.reset()
                snake.reset()
                score.game_over()

screen.exitonclick()
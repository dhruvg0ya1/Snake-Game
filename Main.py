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
restart_requested = False
game_on = True

def on_space():
    """During play: toggle pause. After game over: request restart."""
    global paused, restart_requested, game_on
    if game_on:
        paused = not paused
    else:
        restart_requested = True

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')
screen.onkey(on_space, 'space')

while True:
    game_on = True
    paused = False
    restart_requested = False
    speed = 0.1
    music.play(-1)

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
                score.game_over()
            for i in snake.parts[1:]:
                if snake.head.distance(i) < 1:
                    game_on = False
                    music.stop()
                    hit_sound.play()
                    score.reset()
                    score.game_over()

    while not restart_requested:
        screen.update()
        time.sleep(0.1)

    snake.reset()
    food.refresh()
    score.clear()
    score.goto(0, 280)
    score.write(f'Score: {score.score} High Score: {score.high_score}', False, 'center', ('Courier', 12 , 'normal'))

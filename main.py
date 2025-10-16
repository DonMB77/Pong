from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

def main ():
    screen = Screen()
    screen.setup(800,600)
    screen.bgcolor("black")
    screen.title("Pong Game!")
    screen.tracer(0)
    paddle_r = Paddle(350, 0)
    paddle_l = Paddle(-350, 0)
    ball = Ball()
    screen.listen()
    screen.onkey(paddle_r.go_up, "Up")
    screen.onkey(paddle_r.go_down, "Down")
    screen.onkey(paddle_l.go_up, "w")
    screen.onkey(paddle_l.go_down, "s")
    is_game_on = True
    while is_game_on:
        screen.update()
    is_game_on = True
    return 0

if __name__ == '__main__':
    main()

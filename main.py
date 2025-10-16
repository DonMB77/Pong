from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

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
        time.sleep(0.1)
        screen.update()
        ball.move()
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce_y_axis()
        if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
            ball.bounce_x_axis()

    is_game_on = True
    return 0

if __name__ == '__main__':
    main()

from turtle import Turtle, Screen
from paddle import Paddle

def main ():
    screen = Screen()
    screen.setup(800,600)
    screen.bgcolor("black")
    screen.title("Pong Game!")
    paddle = Paddle(350, 0)
    screen.exitonclick()
    return 0

if __name__ == '__main__':
    main()

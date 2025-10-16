from turtle import Turtle, Screen

class Paddle:
    def __init__(self, x_pos, y_pos):
        self.paddle = Turtle(shape="square", visible=False)
        self.create_paddle(x_pos, y_pos)

    def create_paddle(self, x_pos, y_pos):
        self.paddle.color("white")
        self.paddle.shapesize(5, 1)
        self.paddle.penup()
        self.paddle.goto(x_pos, y_pos)
        self.paddle.showturtle()

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
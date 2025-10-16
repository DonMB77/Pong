from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.create_ball()
        self.x_movement = 10
        self.y_movement = 10

    def create_ball(self):
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.goto(0,0)

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce_y_axis(self):
        self.y_movement *= -1

    def bounce_x_axis(self):
        self.x_movement *= -1

    def ball_reset(self):
        self.goto(0,0)
        self.bounce_x_axis()
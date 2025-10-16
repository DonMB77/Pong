from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.create_ball()

    def create_ball(self):
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.goto(0,0)
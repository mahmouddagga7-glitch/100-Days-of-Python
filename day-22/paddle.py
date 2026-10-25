from turtle import Turtle

PADDLE_HEIGHT = 1
PADDLE_WIDTH = 5
MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self,x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len= PADDLE_HEIGHT)

    def up(self):
        new_y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), new_y)


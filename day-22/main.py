from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

RIGHT_X_POS = 350
RIGHT_Y_POS = 0
LEFT_X_POS = -350
LEFT_Y_POS = 0

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT_X_POS, RIGHT_Y_POS)
l_paddle = Paddle(LEFT_X_POS, LEFT_Y_POS)
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()








screen.exitonclick()

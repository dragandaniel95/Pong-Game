from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

pad_r = Paddle(350, 0)
pad_l = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(pad_r.up, "Up")
screen.onkey(pad_r.down, "Down")
screen.onkey(pad_l.up, "w")
screen.onkey(pad_l.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(pad_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with l_paddle
    if ball.distance(pad_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the player score
    if ball.xcor() > 400:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_goal()

    if ball.xcor() < -400:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_goal()


screen.exitonclick()

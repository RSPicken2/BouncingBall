import time
import turtle


from ball import Ball, Bounds

width = 500
height = 500


bounds = Bounds(height/2, -height/2, width/2, -width/2)

g = -10

start_x = 0
start_y = 0

radius = 50

energy_conserved = 0.95

def sim_loop(ball, ball_turtle):
    while True:
        vel_y = ball.get_y_vel()
        vel_y += g
        ball.set_y_vel(vel_y)
        ball.update_position(timestep=0.01)
        ball_turtle.setpos(x=ball.get_x(), y=ball.get_y())
        turtle.update()

        time.sleep(0.01)


def run():
    ball = Ball(start_x, start_y, 300, 200, radius, bounds, energy_conserved)
    ball_turtle = turtle.Turtle()
    ball_turtle.shape("circle")

    window = turtle.Screen()
    window.setup(width, height)
    window.bgcolor("lightgray")
    window.tracer(0)

    multiplier = radius/10 # size is 20px by default and we want twice the radius for width
    ball_turtle.shapesize(multiplier, multiplier, outline=None)

    ball_turtle.penup()
    ball_turtle.setpos(x=start_x, y=start_y)
    sim_loop(ball, ball_turtle)



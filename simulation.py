import numpy
import random
import time
import turtle


from ball import Ball, Bounds

width = 500
height = 500


bounds = Bounds(height/2, -height/2, width/2, -width/2)

g = -10

start_x = 0
start_y = 0

ball_num = 5

radius = 10

energy_conserved = 0.95

def handle_ball_collision(b1:Ball, b2:Ball):

    # this is a bodge fix to the balls sometimes sticking together
    b1.x += -b1.x_vel * 0.005
    b1.y += -b1.y_vel * 0.005
    b2.x += -b2.x_vel * 0.005
    b2.y += -b2.y_vel * 0.005

    # get unit vector parallel to the collision (vector between ball centres)
    dist = numpy.sqrt(b1.get_sqr_distance(b2))
    # if 0 distance, use a perfect horizontal collision
    u = b1.get_ball_vector(b2) / dist if dist != 0 else [1, 0]

    # the perpendicular component of the velocity won't change after collision, so we can just focus on the parallel
    b1_para = numpy.dot([b1.x_vel, b1.y_vel], u)
    b2_para = numpy.dot([b2.x_vel, b2.y_vel], u)

    # add new velocities
    # TOTO: implement conservation of momentum with varying mass
    b2.x_vel += (b1_para - b2_para) * u[0] * energy_conserved
    b2.y_vel += (b1_para - b2_para) * u[1] * energy_conserved

    b1.x_vel += (b2_para - b1_para) * u[0] * energy_conserved
    b1.y_vel += (b2_para - b1_para) * u[1] * energy_conserved





def sim_balls(balls, ball_turtles):
    for i in range(len(balls)):
        vel_y = balls[i].get_y_vel()
        vel_y += g
        balls[i].set_y_vel(vel_y)

        balls[i].update_position(timestep=0.01)
        ball_turtles[i].setpos(x=balls[i].get_x(), y=balls[i].get_y())

    # using a set of frozensets here so there are no duplicate collisions
    #   - no cases where there's a record of b1 colliding with b2 and also b2 colliding with b1
    collisions = {frozenset([b1, b2]) for b1 in balls for b2 in balls
                  if b1 != b2 and b1.is_colliding(b2)}

    for col in collisions:
        handle_ball_collision(*col)
        #print(col)

    turtle.update()


def run():
    balls = []
    ball_turtles = []
    for i in range(ball_num):
        balls.append(
            Ball(random.randint(-width/2, width/2), random.randint(-height/2, height/2),
                 random.randint(-200, 200), random.randint(-200, 200),
                 radius, bounds, energy_conserved)
        )

        ball_turtles.append(turtle.Turtle())
        ball_turtles[i].shape("circle")

        multiplier = radius / 10  # size is 20px by default and we want twice the radius for width
        ball_turtles[i].shapesize(multiplier, multiplier, outline=None)

        ball_turtles[i].penup()
        ball_turtles[i].setpos(x=start_x, y=start_y)

    window = turtle.Screen()
    window.setup(width, height)
    window.bgcolor("lightgray")
    window.tracer(0)

    while True:
        sim_balls(balls, ball_turtles)
        time.sleep(0.01)



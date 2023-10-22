from collections import namedtuple


Bounds = namedtuple("bounds", ['top', 'bottom', 'right', 'left'])


class Ball:
    def __init__(self, x, y, x_vel, y_vel, radius, bounds: Bounds, energy_conserved):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius
        self.bounds = bounds
        self.energy_conserved = energy_conserved

    # detects if the ball has collided with the walls and bounces it the other direction
    def handle_collisions(self):
        # detect a collision with left and right walls
        if self.x + self.radius > self.bounds.right:
            print(str(self.get_x()) + " " + str(self.get_y()))
            self.x = self.bounds.right - self.radius
            self.x_vel *= -self.energy_conserved
        elif self.x - self.radius < self.bounds.left:
            print(str(self.get_x()) + " " + str(self.get_y()))
            self.x = self.bounds.left + self.radius
            self.x_vel *= -self.energy_conserved

        # detect a collision with top and bottom walls
        if self.y + self.radius >= self.bounds.top:
            print(str(self.get_x()) + " " + str(self.get_y()))
            self.y = self.bounds.top - self.radius
            self.y_vel *= -self.energy_conserved
        elif self.y - self.radius <= self.bounds.bottom:
            print(str(self.get_x()) + " " + str(self.get_y()))
            self.y = self.bounds.bottom + self.radius
            self.y_vel *= -self.energy_conserved

    def update_position(self, timestep):
        self.x += self.x_vel * timestep
        self.y += self.y_vel * timestep

        self.handle_collisions()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, position):
        self.x = position

    def set_y(self, position):
        self.y = position

    def get_x_vel(self):
        return self.x_vel

    def get_y_vel(self):
        return self.y_vel

    def set_x_vel(self, velocity):
        self.x_vel = velocity

    def set_y_vel(self, velocity):
        self.y_vel = velocity

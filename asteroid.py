import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_change = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_1.velocity = self.velocity.rotate(angle_change) * 1.2
        new_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_2.velocity = self.velocity.rotate(-angle_change) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
       self.position += self.velocity*dt 

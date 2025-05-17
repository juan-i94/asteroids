import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for angle in [rand_angle, -rand_angle]:
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid.velocity = self.velocity.rotate(angle) * 1.2

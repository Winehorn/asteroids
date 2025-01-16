import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20,50)
        velocity_1 = self.velocity.copy().rotate(split_angle) * 1.2
        velocity_2 = self.velocity.copy().rotate(-split_angle) * 1.2

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_2

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color=(255, 255, 255), center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
from circleshape import *
from constants import *
from player import *
import random
import pygame 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        movement = self.velocity * dt
        self.position += movement

    def split(self, asteroids):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2

        asteroids.add(asteroid1)
        asteroids.add(asteroid2)
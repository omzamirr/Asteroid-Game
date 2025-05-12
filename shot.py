from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame


class Shot(CircleShape):

    SHOT_RADIUS = 5

    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, Shot.SHOT_RADIUS)
        self.velocity = velocity


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), Shot.SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt


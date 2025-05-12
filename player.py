
from circleshape import * 
from constants import *
from circleshape import CircleShape
from shot import Shot
import pygame 

PLAYER_SHOOT_COOLDOWN = 0.3

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self, dt, direction=1):
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        print(self.rotation)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(dt, -1)

        if keys[pygame.K_SPACE]:
            self.shoot()


        if self.timer > 0:
            self.timer -= dt

    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction


    def shoot(self):
        if self.timer <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot_position = self.position + forward * self.radius
            velocity = forward * PLAYER_SHOOT_SPEED
            Shot(shot_position, velocity)
            self.timer = PLAYER_SHOOT_COOLDOWN
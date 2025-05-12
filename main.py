from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame
import sys  # Add this import for sys.exit()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collisions(asteroid):
                    bullet.kill()
                    asteroid.split(asteroids)
        
        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()

        print(f"Number of asteroids: {len(asteroids)}")

if __name__ == "__main__":
    main()
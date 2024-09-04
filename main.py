import pygame
from sys import exit
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt) # Update the player's state first
            
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                exit()
            
            for bullet in shots:
                if bullet.is_colliding(asteroid):
                    bullet.kill()
                    asteroid.split()
            
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen) # The draw the player with the updated state
        
        pygame.display.flip()
        
        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()
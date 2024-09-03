import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for player in updatable:
            player.update(dt) # Update the player's state first
            
        screen.fill("black")
        
        for player in drawable:
            player.draw(screen) # The draw the player with the updated state
        
        pygame.display.flip()
        
        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        
        

if __name__ == "__main__":
    main()
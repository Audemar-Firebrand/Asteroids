import pygame
from constants import *
from player import *
def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    Clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        delta_time = Clock.tick(60)
        dt = delta_time / 1000
    

if __name__ == "__main__":
    main()

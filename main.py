import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # set pygame window title
    pygame.display.set_caption("Asteroids")

    # set pygame font
    pygame.font.init()
    gamefont = pygame.font.SysFont('Comic Sans MS', 50)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    score = 0

    bg = (0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update
        for u in updatable:
            u.update(dt)

        # check player
        for a in asteroids:
            if a.collides_with(player):
                print("Game Over!")
                sys.exit()
            for s in shots:
                if a.collides_with(s):
                    score += 1
                    a.split()
                    s.kill()
                    break

        # update text
        text = gamefont.render(str(score), True, "green")

        # draw
        pygame.Surface.fill(screen, bg)
        screen.blit(text, (SCREEN_WIDTH - (5 + (20 * len(str(score)))), 5))
        for d in drawable:
            d.draw(screen)


        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
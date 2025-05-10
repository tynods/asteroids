import sys
import pygame
from pygame.locals import *

from constants import *
from asteroid import Asteroid
from shot import Shot
from player import Player
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    a_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(Color(0,0,0))
        
        updatable.update(dt)
        for x in drawable :
            x.draw(screen)
        
        for a in asteroids:
            for s in shots:
                if a.collides(s):
                    a.split()
                    s.kill()

        for a in asteroids :
            if a.collides(player):
                print("Game over!")
                sys.exit()
        
        pygame.display.flip()
        dt = clk.tick(60)/1000


if __name__ == "__main__":
    main()
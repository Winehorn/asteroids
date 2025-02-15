# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
import constants
import player
import asteroid
import asteroidfield
import shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable,)
    shot.Shot.containers = (updatable, drawable, shots)
    player_obj = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroidfield.AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for obj in updatable:
            obj.update(dt)
        for asteroid_obj in asteroids:
            if asteroid_obj.collides_with(player_obj):
                print("Game over!")
                sys.exit()
            for shot_obj in shots:
                if asteroid_obj.collides_with(shot_obj):
                    asteroid_obj.split()
                    shot_obj.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

    
if __name__ == "__main__":
    main()

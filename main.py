# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_obj = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player_obj.update(dt)
        screen.fill((0, 0, 0))
        player_obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()

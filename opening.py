import sys

from module.constant import *
from module.material import Button
import game_off


def main():
    pygame.init()
    pygame.display.set_caption("cerke")
    screen = pygame.display.set_mode(Const.DISPLAY_SIZE)

    off_button = Button("field", (100, 100))
    off_button.set_point((595, 315))

    while True:
        screen.fill((255, 255, 255))
        screen.blit(off_button.image, off_button.rect)

        for event in pygame.event.get():
            # GUI operation
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if off_button.collide(event.pos):
                    game_off.main()

        pygame.display.update()


if __name__ == "__main__":
    main()

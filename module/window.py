import sys

import pygame
from pygame.locals import *

from module.constant import *


def locator(point):
    if point[0] <= 140:
        dest_x = 30
    elif point[0] < Const.DISPLAY_SIZE[0]-140:
        dest_x = point[0]-140
    else:
        dest_x = Const.DISPLAY_SIZE[0]-310

    if point[1] > Const.DISPLAY_SIZE[1]-140:
        dest_y = Const.DISPLAY_SIZE[1]-170
    else:
        dest_y = point[1]

    return dest_x, dest_y


class MessageBox:
    def __init__(self, size, color):
        self.base_window = pygame.Surface(size, flags=pygame.SRCALPHA)
        self.base_window.set_alpha(0)
        self.base_window.fill((0, 0, 0, 127))
        self.base_window.fill(color, (1, 1, size[0]-2, size[1]-2))


class InputBox(MessageBox):
    def __init__(self, size, color):
        super().__init__(())


# message window to ask a two-choice problem
class Window(MessageBox):
    BUTTON = pygame.Surface((130, 50), flags=pygame.SRCALPHA)
    BUTTON.set_alpha(0)
    BUTTON.fill((0, 0, 0))
    BUTTON.fill((245, 245, 230), (1, 1, 128, 48))

    """
    ques_tuple: (pygame.Font, (pos_x, pos_y))
    choice_list: {"Yes": (pygame.Font, (pos_x, pos_y)
                  "No": (pygame.Font, (pos_x, pos_y)}
    """
    def __init__(self, size, color, ques_tuple: tuple, choice_list):
        super().__init__(size, color)
        self.ques = ques_tuple[0]
        self.ques_pos_x = ques_tuple[1][0]
        self.ques_pos_y = ques_tuple[1][1]
        self.yes = choice_list["Yes"][0]
        self.yes_pos_x = choice_list["Yes"][1][0]
        self.yes_pos_y = choice_list["Yes"][1][1]
        self.no = choice_list["No"][0]
        self.no_pos_x = choice_list["No"][1][0]
        self.no_pos_y = choice_list["No"][1][1]

    def render(self, screen, point) -> bool:
        dest_x, dest_y = locator(point)

        while True:
            screen.blit(self.base_window, (dest_x, dest_y))
            screen.blit(Window.BUTTON, (dest_x+8, dest_y+80))
            screen.blit(Window.BUTTON, (dest_x+142, dest_y+80))
            screen.blit(
                self.ques,
                (dest_x + self.ques_pos_x, dest_y + self.ques_pos_y)
            )
            screen.blit(
                self.yes,
                (dest_x + self.yes_pos_x, dest_y + self.yes_pos_y)
            )
            screen.blit(
                self.no,
                (dest_x + self.no_pos_x, dest_y + self.no_pos_y)
            )

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        return False
                    if event.key == K_y:
                        return True
                    if event.key == K_n:
                        return False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if dest_y+80 <= y and y <= dest_y+130:
                        if dest_x+8 <= x and x <= dest_x+138:
                            return True
                        if dest_x+142 <= x and x <= dest_x+278:
                            return False
            pygame.display.update()

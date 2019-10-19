import sys

import pygame
from pygame.locals import *

from module.constant import *
from module.variable import *
from module.material import redo, undo
from module.window import InputBox
from module.hand import *


def text_render(text):
    return FontSet.FONT_FILE.render(text, True, (0, 0, 0))


def main(path: str):
    pygame.init()
    screen = pygame.display.set_mode(Const.DISPLAY_SIZE)
    pygame.display.set_caption(FontSet.CAPTION)
    board = pygame.image.load("image\\field.png").convert_alpha()
    piece_space = Space(User.SPACE_COLOR, Const.SPACE_SIZE)
    input_img = text_render("Enter the name of the score file")

    while True:
        screen.fill((255, 160, 122))
        screen.blit(board, Const.BOARD_DEST)
        piece_space.render(screen, (0, 0))
        piece_space.render(screen, (911, 0))
        screen.blit(input_img, (530, 300))

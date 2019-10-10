import os

import pygame
from pygame.locals import *

from module.constant import *

pygame.init()


class Material:
    def __init__(self, name: str, size: tuple):
        self.name = name
        self.size = size


class Space(Material):
    def __init__(self, color: tuple, size: tuple):
        super().__init__("", size)
        self.image = pygame.Surface(self.size)
        self.image.fill(color)

    def render(self, screen, pos: tuple):
        screen.blit(self.image, pos)


class Button(Material):
    def __init__(self, name: str, size: tuple, extention: str = ".png"):
        super().__init__(name, size)
        self.path = os.getcwd() + "\\image\\" + name + extention
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

    def set_point(self, location: tuple):
        self.rect.center = location

    def collide(self, signal: tuple) -> bool:
        if self.rect.collidepoint(signal):
            return True
        else:
            return False


class Piece(Material):
    NAME = (
        "nuak", "io", "uai", "tuk", "kua", "maun", "dau", "kaun", "gua", "kauk"
    )
    COLOR = ("black", "red")
    DIRECTION = (0, 1)  # 0 means up, 1 means down

    def __init__(self, name: str, color: str, direction: int):
        super().__init__(name, (64, 64))
        self.color = color
        self.direction = direction
        self.path = os.getcwd() + "\\image\\piece\\" + color[0] + name + ".png"
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        if direction == 2:
            self.image = pygame.transform.rotate(self.image, 270)
        elif direction == 1:
            self.image = pygame.transform.rotate(self.image, 180)

    def move(self, dest: tuple):
        self.rect.center = dest

    def reverse(self):
        self.image = pygame.transform.rotate(self.image, 180)
        self.direction ^= 1

    @staticmethod
    def load(player_color: int) -> list:
        ret_list = []   # piece object is appended here
        if player_color == "black":
            INIT_POS = Const.TAM_POS + Const.NUAK_IO_POS[0] + Const.OTHER_POS
        else:
            INIT_POS = Const.TAM_POS + Const.NUAK_IO_POS[1] + Const.OTHER_POS

        ret_list.append(Piece("tam", "black", 2))
        for name in Piece.NAME:
            for color in Piece.COLOR:
                # nuak and io exist only 1 for each color
                if name == "nuak" or name == "io":
                    # if piece's color is player's color, the piece is up
                    if Const.COLOR_TO_NUM[color] == player_color:
                        tmp_obj = Piece(name, color, 0)
                    # if not, down
                    else:
                        tmp_obj = Piece(name, color, 1)
                    ret_list.append(tmp_obj)
                    continue
                for dir in Piece.DIRECTION:
                    # kauk exists 4 for each color and direction
                    if name == "kauk":
                        for _ in range(3):
                            ret_list.append(Piece(name, color, dir))
                    ret_list.append(Piece(name, color, dir))
        for piece, pos in zip(ret_list, INIT_POS):
            piece.rect.center = pos
        return ret_list

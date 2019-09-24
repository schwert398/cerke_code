import os
from copy import deepcopy
import pygame
from pygame.locals import *
from module.class_constant import *
from module.class_variable import *

pygame.init()

class Piece:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color
        if color is None:
            self.path = os.getcwd() + "\\image\\piece\\" + name + ".png"
        else:
            self.path = os.getcwd() + "\\image\\piece\\" + (color[0] + name) + ".png"
    
    def generate(self, direction):    # 画像の読み込みと回転・リサイズ
        tmp = pygame.image.load(self.path).convert_alpha()
        tmp = pygame.transform.scale(tmp, (64, 64))
        if direction == "right":
            tmp = pygame.transform.rotate(tmp, 270)
        elif direction == "down":
            tmp = pygame.transform.rotate(tmp, 180)
        rect_tmp = tmp.get_rect()
        return tmp, rect_tmp, self.color, direction, self.name
    
    @staticmethod
    def load(player_color):
        piece_img = []     # 表示用の駒の情報
        tamFlag = False     # 皇を読み込んだか
        Index = 0           # 何番目の駒か
        for col in Const.color:
            for nam in Const.name:
                if nam == "tam":
                    if tamFlag:
                        continue
                    tmp_obj = Piece("tam")
                    piece_img.append(tuple(tmp_obj.generate("right")))
                    piece_img[-1][1].center = Const.init_pos[0][Index]
                    tamFlag = True
                    Index += 1
                    continue
                elif nam == "nuak":    # 船は1枚ずつ
                    tmp_obj = Piece("nuak", col)
                    if col == "black":
                        if player_color: piece_img.append(tuple(tmp_obj.generate("down")))
                        else: piece_img.append(tuple(tmp_obj.generate("up")))
                    else:
                        if player_color: piece_img.append(tuple(tmp_obj.generate("up")))
                        else: piece_img.append(tuple(tmp_obj.generate("down")))
                    piece_img[-1][1].center = Const.init_pos[0][Index]
                    Index += 1
                    continue
                elif nam == "io":     # 王も1枚ずつ
                    tmp_obj = Piece("io", col)
                    if col == "black":
                        if player_color: piece_img.append(tuple(tmp_obj.generate("down")))
                        else: piece_img.append(tuple(tmp_obj.generate("up")))
                    else:
                        if player_color: piece_img.append(tuple(tmp_obj.generate("up")))
                        else: piece_img.append(tuple(tmp_obj.generate("down")))
                    piece_img[-1][1].center = Const.init_pos[0][Index]
                    Index += 1
                    continue
                for direc in Const.direction:
                    tmp_obj = Piece(nam, col)
                    if nam == "kauk":   # 兵は同色同向で4枚要るため、3回分補う
                        for _ in range(3):
                            piece_img.append(tuple(tmp_obj.generate(direc)))
                            piece_img[-1][1].center = Const.init_pos[0][Index]
                            Index += 1
                    piece_img.append(tuple(tmp_obj.generate(direc)))
                    piece_img[-1][1].center = Const.init_pos[0][Index]
                    Index += 1
        for piece, piece_pos in zip(piece_img, Const.init_pos[User.PL_color]):
            piece[1].center = piece_pos
        return piece_img

    @staticmethod
    def copy(piece_tuple):
        ret = [(item[0].copy(),
                item[1].copy(),
                deepcopy(item[2]),
                deepcopy(item[3]),
                deepcopy(item[4]))
               for item in piece_tuple]
        return ret
        

import os
import pygame
from pygame.locals import *
from class_constant import Constant as Cst

class Piece:
    def __init__(self, name, color=None):
        if color is None: self.path = os.getcwd() + "\\image\\piece\\" + name + ".png"
        else: self.path = os.getcwd() + "\\image\\piece\\" + color + name + ".png"
    
    def generate(self, direction):    # 画像の読み込みと回転・リサイズ
        tmp = pygame.image.load(self.path).convert_alpha()
        tmp = pygame.transform.scale(tmp, (64, 64))
        if direction == "right":
            tmp = pygame.transform.rotate(tmp, 270)
        elif direction == "down":
            tmp = pygame.transform.rotate(tmp, 180)
        rect_tmp = tmp.get_rect()
        return tmp, rect_tmp
    
    def load(self=None):    # SurfaceとRectのtupleを保持したlistオブジェクトを返す
        piece_img = []     # 表示用の駒の情報
        tamFlag = False     # 皇を読み込んだか
        for col in Cst.color:
            for nam in Cst.name:
                if nam == "tam":
                    if tamFlag:
                        continue
                    tmp_obj = Piece("tam")
                    piece_img.append(tuple(tmp_obj.generate("right")))
                    tamFlag = True
                    continue
                elif nam == "nuak":    # 船は1枚ずつ
                    tmp_obj = Piece("nuak", col)
                    if col == "b":
                        piece_img.append(tuple(tmp_obj.generate("up")))
                    else:
                        piece_img.append(tuple(tmp_obj.generate("down")))
                    continue
                elif nam == "io":     # 王も1枚ずつ
                    tmp_obj = Piece("io", col)
                    if col == "b":
                        piece_img.append(tuple(tmp_obj.generate("up")))
                    else:
                        piece_img.append(tuple(tmp_obj.generate("down")))
                    continue
                for direc in Cst.direction:
                    tmp_obj = Piece(nam, col)
                    if nam == "kauk":   # 兵は同色同向で4枚要るため、3回分補う
                        for _ in range(3):
                            piece_img.append(tuple(tmp_obj.generate(direc)))
                    piece_img.append(tuple(tmp_obj.generate(direc)))
        return piece_img

class Space:
    @staticmethod
    def load(color):    # colorで塗りつぶした画像のRectを返す
        spc = pygame.Surface(Cst.space_size)
        spc.fill(color)
        return spc

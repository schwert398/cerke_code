import pygame
from pygame.locals import *
from class_constant import Constant as Cst

class Move:
    def point_search(self=None, x, y):   # 81マスの全探索
        ret_v, ret_h = 0, 0
        for v in Cst.vertical:
            if v-35 <= x <= v+35:
                ret_v = v
                break
        for h in Cst.horizontal:
            if h-35 <= y <= h+35:
                ret_h = h
                break
        if ret_v == 0: return False, False
        return ret_v, ret_h
    
    

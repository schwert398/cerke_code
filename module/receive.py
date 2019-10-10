import sys

import pygame
from pygame.locals import *

from module.constant import *


class Receive:
    @staticmethod
    def receive():
        for event in pygame.event.get():
            # GUI operation
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # left click (return tuple)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                x_flag, y_flag = False, False
                for v in Const.VERTICAL:
                    if v-35 <= x <= v+35:
                        x_flag = True
                        ret_v = v
                        break
                for h in Const.HORIZONTAL:
                    if h-35 <= y <= h+35:
                        y_flag = True
                        ret_h = h
                        break
                if x_flag and y_flag:
                    return ret_v, ret_h
                else:
                    return x, y
            # right click (equals space)
            if event.type == MOUSEBUTTONDOWN and event.button == 2:
                return "space"

            # keyboard operation
            if event.type == KEYDOWN:
                # Esc terminates program
                if event.key == K_ESCAPE:
                    return "terminate"
                # space cancels all choise
                if event.key == K_SPACE:
                    return "space"
                # z undoes
                if event.key == K_z:
                    return "undo"
                # q redoes
                if event.key == K_q:
                    return "redo"
                # a terminates current turn
                if event.key == K_a:
                    return "alter"
                # r reverses selecting piece
                if event.key == K_r:
                    return "rotate"
                # i restarts game
                if event.key == K_i:
                    return "initialize"
                # c make a judgement
                if event.key == K_c:
                    return "ciurl"
                # p, m change score
                if event.key == K_p or event.key == K_KP_PLUS:
                    return "plus"
                if event.key == K_m or event.key == K_KP_MINUS:
                    return "minus"
                # 0, 1 change rate
                if event.key == K_0:
                    return "decrease"
                if event.key == K_1:
                    return "increase"
                # t ends the set
                if event.key == K_t:
                    return "taxt"

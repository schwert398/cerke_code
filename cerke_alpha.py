import sys
from copy import deepcopy
from collections import deque
import pygame
from pygame.locals import *
from class_material import *
from class_recieve import *
from class_constant import Constant as Cst

def main():
    pygame.init()
    screen = pygame.display.set_mode((1051, 631))
    pygame.display.set_caption("机戦")
    board = pygame.image.load("image\\field.png").convert_alpha()
    rect_board, rect_board.center = board.get_rect(), (525, 315)
    backImg = pygame.image.load("image\\backImg.jpg").convert_alpha()
    backImg = pygame.transform.scale(backImg, (631, 631))
    rect_backImg, rect_backImg.center = backImg.get_rect(), (525, 315)
    
    board_info = deque([list(Cst.init_pos)], 10)    # 駒の位置情報(最新10件)
    piece_img = Piece.load()    # 駒の画像と座標の情報
    selector = False    # 選択中か
    choosing = None     # 選択しているのが何か(これはindexとRectのtupleオブジェクト)
    
    while True:
        screen.fill((255, 212, 69, 0))
        screen.blit(backImg, rect_backImg)
        screen.blit(board, rect_board)
        
        for point, img_list in zip(board_info[-1], piece_img):
            img_list[1].center = point
        for img, rect in piece_img:
            screen.blit(img, rect)
        
        pygame.display.update()
        tmp = Recieve.recieve()
        if not (tmp is None):
            if type(tmp) == str:
                if selector and tmp == "rotate":
                    for img, rect in piece_img:
                        if choosing[1] is rect:
                            piece_img[choosing[0]] = (pygame.transform.rotate(img, 180), rect)
                            selector, choosing = False, None
                            break
                if selector and tmp == "space":
                    selector, choosing = False, None
                if tmp == "undo":
                    if len(board_info) != 1: board_info.pop()
                    else: print("no longer undo")
                    selector, choosing = False, None
                if tmp == "initialize":
                    board_info.append(list(Cst.init_pos))
                    selector, choosing = False, None
            if type(tmp) == tuple:
                if selector:
                    tmp_info = deepcopy(board_info[-1])
                    tmp_info[choosing[0]] = tmp
                    board_info.append(tmp_info)
                    selector, choosing = False, None
                else:
                    for idx, item in enumerate(piece_img):
                        if item[1].collidepoint(tmp[0], tmp[1]):
                            selector = True
                            choosing = (idx, item[1])
                            break
        
if __name__ == "__main__":
    main()

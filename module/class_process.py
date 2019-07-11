from copy import deepcopy
from random import randint
import pygame
from pygame.locals import *
from module.class_constant import *

class Process:
    # キー操作の処理
    @staticmethod
    def process_str(signal, board_info, piece_img, undo_repository, lang, msg_list, 
                    msg_queue, turn, selector, choosing, score, rate):
        if selector and signal == "rotate":
            for img, rect in piece_img:
                if choosing[1] is rect:
                    piece_img[choosing[0]] = (pygame.transform.rotate(img, 180), rect)
                    selector, choosing = False, None
                    break
        if signal == "space":
            selector, choosing = False, None
        
        if signal == "alter":
            turn ^= 1
        
        if signal == "undo":
            if len(board_info) != 1:
                undo_repository.append(board_info.pop())
                turn ^= 1
            else:
                if lang == 1:   # リパライン語のとき
                    msg_queue.append(msg_list[0])
                    msg_queue.append(msg_list[1])
                else:           # その他のとき
                    msg_queue.append(msg_list[0])
            selector, choosing = False, None
        
        if signal == "redo":
            if len(undo_repository) != 0:
                board_info.append(undo_repository.pop())
                turn ^= 1
            else:
                if lang == 1:
                    msg_queue.append(msg_list[2])
                    msg_queue.append(msg_list[3])
                else:
                    msg_queue.append(msg_list[1])
            selector, choosing = False, None
        
        if signal == "plus":
            score += 1
        if signal == "minus":
            score -= 1
        
        if signal == "decrease":
            rate -= 1
        if signal == "increase":
            rate += 1
        
        if signal == "initialize":
            board_info.append(list(Const.init_pos))
            undo_repository.clear()
            selector, choosing = False, None
            turn = 0
        
        if signal == "ciurl":
            ret = 0
            for _ in range(5):
                ret += randint(0, 1)
            msg_queue.append(str(ret))
        for point, img_list in zip(board_info[-1], piece_img):
            img_list[1].center = point
        return board_info, undo_repository, msg_queue, turn, selector, choosing, score, rate
    
    # マウス操作の処理
    @staticmethod
    def process_tuple(signal, board_info, piece_img, undo_repository, lang, msg_list,
                      msg_queue, turn, selector, choosing):
        if selector:
            for idx, item in enumerate(piece_img):
                if item[1].collidepoint(signal[0], signal[1]):
                    if lang == 1:
                        msg_queue.append(msg_list[4])
                        msg_queue.append(msg_list[5])
                    else: msg_queue.append(msg_list[2])
                    selector, choosing = False, None
                    return board_info, undo_repository, msg_queue, turn, selector, choosing
                
            tmp_info = deepcopy(board_info[-1])
            tmp_info[choosing[0]] = signal
            board_info.append(tmp_info)
            undo_repository.clear()
            selector, choosing = False, None
            turn ^= 1
        else:
            for idx, item in enumerate(piece_img):
                if item[1].collidepoint(signal[0], signal[1]):
                    selector = True
                    choosing = (idx, item[1])
        for point, img_list in zip(board_info[-1], piece_img):
            img_list[1].center = point
        return board_info, undo_repository, msg_queue, turn, selector, choosing

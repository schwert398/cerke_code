from collections import deque

import pygame
from pygame.locals import *

from module.constant import *
from module.material import *
from module.receive import *
from module.variable import *
from module.render import *
from module.process import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(Const.DISPLAY_SIZE)
    pygame.display.set_caption(FontSet.CAPTION)
    board = pygame.image.load("image\\field.png").convert_alpha()
    piece_space = Space(User.SPACE_COLOR, Const.SPACE_SIZE)

    # generate objects
    piece_obj_list = Piece.load(User.PL_COLOR)    # list of Piece object
    msg_queue = deque([], 5)    # message log (latest 5)
    hand_queue = []  # list holding the operations done
    undo_queue = []  # list holding the operations poped from hand_queue
    queue_holder = [msg_queue, hand_queue, undo_queue]

    # generate flags (these are all either of False or int)
    selecting = False   # if selecting a piece (int shows index)
    flag_judge = False  # if judged in the turn (int shows num of judgement)
    flag_step = False   # if stepped over a piece in the turn (int shows index)
    flag_box = [selecting, flag_judge, flag_step]

    # generate param
    rate = 1  # score rate
    score = User.BLACK_SCORE    # score of black side
    turn = User.FIRST_HAND      # which side move in the turn (0 means black)
    parameter_box = [rate, score, turn]

    while True:
        screen.fill(User.BG_COLOR)
        screen.blit(board, Const.BOARD_DEST)
        piece_space.render(screen, (0, 0))
        piece_space.render(screen, (911, 0))

        Render.render(
            screen, piece_obj_list, queue_holder, flag_box, parameter_box
        )
        pygame.display.update()

        signal = Receive.receive()
        if signal is None:
            continue
        elif signal == "terminate":
            return
        elif type(signal) == str:
            ret = Process.proc_str(
                screen, signal,
                piece_obj_list, queue_holder, flag_box, parameter_box
            )
        elif type(signal) == tuple:
            ret = Process.proc_tuple(
                screen, signal,
                piece_obj_list, queue_holder, flag_box, parameter_box
            )
        if ret is None:
            continue
        piece_obj_list, queue_holder, flag_box, parameter_box = ret


if __name__ == "__main__":
    main()

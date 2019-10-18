from copy import deepcopy
from random import randint

import pygame
from pygame.locals import *

from module.hand import *
from module.window import *
from module.material import *
from module.constant import *
from module.variable import *


def hand_pos_provider(piece_obj_list: list, turn: int) -> pygame.Rect:
    # search the youngest indexed hand pos which isn't occupied
    for rect in Const.HAND_POS[turn]:
        if rect.collidelist(piece_obj_list) == -1:
            return rect


def get_piece(getter: Piece, target: Piece, target_dest: pygame.Rect):
    if getter.direction == target.direction:
        return
    getter.move(target.rect.center)
    target.move(target_dest.center)
    target.reverse()


def undo(hand: str, piece_obj_list: list, turn: int):
    # 3rd arg turn means player after undo
    act, dest, target_pos_index = Hand.parser(hand)
    act_index = pygame.Rect(dest, (0, 0)).collidelist(piece_obj_list)
    piece_obj_list[act_index].move(act)

    # if getting happened
    if target_pos_index != -1:
        target_pos = Const.HAND_POS[turn][target_pos_index]
        target_index = target_pos.collidelist(piece_obj_list)
        piece_obj_list[target_index].move(dest)
        piece_obj_list[target_index].reverse()


def redo(hand: str, piece_obj_list: list, turn: int):
    # 3rd arg turn means player before redo
    act, dest, target_pos_index = Hand.parser(hand)
    act_index = pygame.Rect(act, (0, 0)).collidelist(piece_obj_list)
    # if getting happened
    if target_pos_index != -1:
        target_index = pygame.Rect(dest, (0, 0)).collidelist(piece_obj_list)
        get_piece(
            piece_obj_list[act_index],
            piece_obj_list[target_index],
            Const.HAND_POS[turn][target_pos_index]
        )
    else:
        piece_obj_list[act_index].move(dest)


class Process:
    GET_WINDOW = Window(
        FontSet.WINDOW_MSG_DICT["get?"], FontSet.YES_NO_DICT
    )
    STEP_WINDOW = Window(
        FontSet.WINDOW_MSG_DICT["step?"], FontSet.YES_NO_DICT,
    )
    ABONDON_WINDOW = Window(
        FontSet.WINDOW_MSG_DICT["abondon?"], FontSet.YES_NO_DICT,
    )
    FINISH_WINDOW = Window(
        FontSet.WINDOW_MSG_DICT["finish?"], FontSet.YES_NO_DICT,
    )
    RECORD_WINDOW = Window(
        FontSet.WINDOW_MSG_DICT["record?"], FontSet.YES_NO_DICT,
    )

    # processes of key operations
    @staticmethod
    def proc_str(screen, signal: str,
                 piece_obj_list, queue_holder, flag_box, param_box):
        msg_queue, hand_queue, undo_queue = queue_holder
        selecting, flag_judge, flag_step = flag_box
        rate, score, turn = param_box

        if signal == "taxt":
            if len(hand_queue) == 0:
                return
            if_finish = Process.FINISH_WINDOW.render(screen, (595, 245))
            if if_finish is True:
                print(hand_queue)
                if User.RECORD == "on":
                    Hand.output(hand_queue)
                signal = "initialize"
            elif if_finish is False:
                hand_queue[-1] += "=tymorko"

        if signal == "space":
            selecting, flag_judge, flag_step = False, False, False

        if signal == "alter":
            if_abondon = Process.ABONDON_WINDOW.render(screen, (595, 245))
            if if_abondon:
                if flag_judge:
                    choice = piece_obj_list[selecting]
                    if flag_step:
                        bridge = piece_obj_list[flag_step]
                        tmp_hand = Hand.record(
                            choice, choice, bridge, flag_judge
                        )
                    else:
                        tmp_hand = Hand.record(
                            choice, choice, flag_step, flag_judge
                        )
                    hand_queue.append(tmp_hand)
                else:
                    hand_queue.append("passed for some unknown reason")
            selecting, flag_judge, flag_step = False, False, False
            turn ^= 1

        if signal == "undo":
            if len(hand_queue) > 0:
                turn ^= 1
                last_hand = hand_queue.pop()
                undo(last_hand, piece_obj_list, turn)
                undo_queue.append(last_hand)
            else:
                msg_queue.extend(FontSet.LOG_MSG_DICT["oldest"])
            selecting, flag_judge, flag_step = False, False, False

        if signal == "redo":
            if len(undo_queue) != 0:
                next_hand = undo_queue.pop()
                redo(next_hand, piece_obj_list, turn)
                hand_queue.append(next_hand)
                turn ^= 1
            else:
                msg_queue.extend(FontSet.LOG_MSG_DICT["newest"])
            selecting, flag_judge, flag_step = False, False, False

        if signal == "plus":
            score += 1
        if signal == "minus":
            score -= 1

        if signal == "decrease":
            rate -= 1
        if signal == "increase":
            rate += 1

        if signal == "initialize":
            piece_obj_list = Piece.load(User.PL_COLOR)
            hand_queue = []
            undo_queue.clear()
            selecting, flag_judge, flag_step = False, False, False
            rate = 1
            turn = User.FIRST_HAND

        if signal == "ciurl":
            if flag_judge is not False:
                msg_queue.extend(FontSet.LOG_MSG_DICT["judged"])
            else:
                ret = 0
                for _ in range(5):
                    ret += randint(0, 1)
                msg_queue.extend(FontSet.NUMBER_DICT[ret])
                flag_judge = ret

        queue_holder = [msg_queue, hand_queue, undo_queue]
        flag_box = [selecting, flag_judge, flag_step]
        param_box = [rate, score, turn]
        return piece_obj_list, queue_holder, flag_box, param_box

    # processes of mouse operations
    @staticmethod
    def proc_tuple(screen, signal: tuple,
                   piece_obj_list, queue_holder, flag_box, param_box):
        msg_queue, hand_queue, undo_queue = queue_holder
        selecting, flag_judge, flag_step = flag_box
        rate, score, turn = param_box

        signal_rect = pygame.Rect(signal, (1, 1))

        # if selecting a piece
        if selecting is not False:
            choice = piece_obj_list[selecting]
            collide_index = signal_rect.collidelist(piece_obj_list)
            # if any piece touches signal
            if collide_index >= 0:
                target = piece_obj_list[collide_index]
                # if signal is target
                if selecting == collide_index:
                    msg_queue.extend(FontSet.LOG_MSG_DICT["colliding"])
                # if target is opponent's piece (or tam)
                elif target.direction != turn:
                    if_get = Process.GET_WINDOW.render(screen, signal)
                    if if_get:
                        if flag_step:
                            bridge = piece_obj_list[flag_step]
                            tmp_hand = Hand.record(
                                choice, signal, bridge, flag_judge
                            )
                        else:
                            tmp_hand = Hand.record(
                                choice, signal, flag_step, flag_judge
                            )
                        # avoid unexpected error
                        if tmp_hand is False:
                            return None
                        # UPDATE AFTER RECORDING THE SCORE
                        target_dest = hand_pos_provider(piece_obj_list, turn)
                        get_piece(choice, target, target_dest)
                        hand_queue.append(tmp_hand)
                        hand_queue[-1] += "${}".format(
                            Const.HAND_POS[turn].index(target_dest)
                        )
                        turn ^= 1
                        undo_queue.clear()

                        queue_holder = [msg_queue, hand_queue, undo_queue]
                        flag_box = [False]*3
                        param_box = [rate, score, turn]
                        return (
                            piece_obj_list, queue_holder, flag_box, param_box
                        )
                    if flag_step:
                        return None
                    if_step = Process.STEP_WINDOW.render(screen, signal)
                    if if_step:
                        flag_step = collide_index

                        queue_holder = [msg_queue, hand_queue, undo_queue]
                        flag_box = [selecting, flag_judge, flag_step]
                        param_box = [rate, score, turn]
                        return (
                            piece_obj_list, queue_holder, flag_box, param_box
                        )
                # if target is yours
                else:
                    if flag_step is not False:
                        msg_queue.extend(FontSet.LOG_MSG_DICT["colliding"])
                        queue_holder = [msg_queue, hand_queue, undo_queue]
                        return (
                            piece_obj_list, queue_holder, flag_box, param_box
                        )
                    if_step = Process.STEP_WINDOW.render(screen, signal)
                    if if_step:
                        flag_step = collide_index
                        flag_box = [selecting, flag_judge, flag_step]
                        return (
                            piece_obj_list, queue_holder, flag_box, param_box
                        )
            # if no piece touches signal
            else:
                if flag_step is not False:
                    bridge = piece_obj_list[flag_step]
                    tmp_hand = Hand.record(
                        choice, signal, bridge, flag_judge
                    )
                else:
                    tmp_hand = Hand.record(
                        choice, signal, flag_step, flag_judge
                    )
                # !!! UPDATE AFTER RECORDING THE HAND !!!
                choice.move(signal)
                if tmp_hand is False:
                    return None
                hand_queue.append(tmp_hand)
                turn ^= 1
                undo_queue.clear()

                queue_holder = [msg_queue, hand_queue, undo_queue]
                flag_box = [False]*3
                param_box = [rate, score, turn]
            return piece_obj_list, queue_holder, flag_box, param_box
        # if not selecting any piece
        else:
            collide_index = signal_rect.collidelist(piece_obj_list)
            if collide_index >= 0:
                selecting = collide_index

            queue_holder = [msg_queue, hand_queue, undo_queue]
            flag_box = [selecting, flag_judge, flag_step]
            param_box = [rate, score, turn]
            return (
                piece_obj_list, queue_holder, flag_box, param_box
            )

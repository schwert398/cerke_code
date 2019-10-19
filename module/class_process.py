from copy import deepcopy
from random import randint
import pygame
from pygame.locals import *
from module.class_hand import *
from module.class_window import *
from module.class_material import *
from module.class_constant import *
from module.class_variable import *

class Process:
    get_window = Window(FontSet.window_msg_list[0], FontSet.yes_no_list)
    step_window = Window(FontSet.window_msg_list[1], FontSet.yes_no_list)
    abondon_window = Window(FontSet.window_msg_list[2], FontSet.yes_no_list)
    finish_window = Window(FontSet.window_msg_list[3], FontSet.yes_no_list)
    
    # キー操作の処理
    @staticmethod
    def proc_str(signal, screen, queue_holder, flag_box, param_box):
        msg_queue, object_queue, undo_queue = queue_holder
        piece_img, board_info, hand, hand_num_box = object_queue[-1]
        selector, choosing, flag_judged, flag_step = flag_box
        rate, score, turn = param_box
        
        if signal == "taxt":
            if_finish = Process.finish_window.render(screen, (595, 245))
            if if_finish:
                if User.record == "on":
                    hand[-1] += "=taxt"
                    Hand.output(hand)
                signal = "initialize"
        
        if signal == "space":
            selector, choosing, flag_judged, flag_step = False, None, False, False
        
        if signal == "alter":
            if flag_judged:
                if_abondon = Process.abondon_window.render(screen, (595, 245))
                if if_abondon:
                    hand = Hand.record(hand, piece_img[choosing[0]], piece_img[choosing[0]], flag_step, flag_judged)
                    turn ^= 1
            else:
                turn ^= 1
        
        if signal == "undo":
            if len(object_queue) != 1:
                turn ^= 1
                undo_queue.append(object_queue.pop())
            else:
                msg_queue.extend(FontSet.log_msg_dict["oldest"])
            selector, choosing, flag_judged, flag_step = False, None, False, False
        
        if signal == "redo":
            if len(undo_queue) != 0:
                turn ^= 1
                object_queue.append(undo_queue.pop())
            else:
                msg_queue.extend(FontSet.log_msg_dict["newest"])
            selector, choosing, flag_judged, flag_step = False, None, False, False
        
        if signal == "plus":
            score += 1
        if signal == "minus":
            score -= 1
        
        if signal == "decrease":
            rate -= 1
        if signal == "increase":
            rate += 1
        
        if signal == "initialize":
            piece_img = Piece.load(User.PL_color)
            board_info = list(Const.init_pos[User.first_hand])
            hand = []
            hand_num_box = [0, 0]
            object_queue.append([piece_img, board_info, hand, hand_num_box])
            undo_queue.clear()
            selector, choosing, flag_judged, flag_step = False, None, False, False
            rate = 1
            turn = User.first_hand
        
        if signal == "ciurl":
            if flag_judged is not False:
                msg_queue.extend(FontSet.log_msg_dict["judged"])
            else:
                ret = 0
                for _ in range(5):
                    ret += randint(0, 1)
                msg_queue.append(FontSet.font_file.render(str(ret), True, (0, 0, 0)))
                flag_judged = ret
        for point, img_list in zip(board_info, piece_img):
            img_list[1].center = point
        queue_holder = [msg_queue, object_queue, undo_queue]
        flag_box = [selector, choosing, flag_judged, flag_step]
        param_box = [rate, score, turn]
        parameter_box = [rate, score, turn]
        return queue_holder, flag_box, param_box
    
    # マウス操作の処理
    @staticmethod
    def proc_tuple(signal, screen, queue_holder, flag_box, param_box):
        msg_queue, object_queue, undo_queue = queue_holder
        piece_img, board_info, hand, hand_num_box = object_queue[-1]
        selector, choosing, flag_judged, flag_step = flag_box
        rate, score, turn = param_box

        # piece_imgとboard_infoをコピーする
        tmp_piece = Piece.copy(piece_img)
        tmp_info = deepcopy(board_info)
        tmp_hand = deepcopy(hand)
        tmp_box = deepcopy(hand_num_box)
        
        if selector:
            for idx, item in enumerate(tmp_piece):
                if item[1].collidepoint(signal[0], signal[1]):
                    if item[3] != Const.num_to_dir[turn]: # 相手の駒に当たったとき
                        if_get = Process.get_window.render(screen, signal)
                        if if_get:
                            tmp_piece[idx] = (pygame.transform.rotate(item[0], 180),
                                              item[1],
                                              item[2],
                                              Const.num_to_dir[Const.dir_to_num[item[3]]^1],
                                              item[4])
                            tmp_info[idx] = Const.hand_pos[turn^1][tmp_box[turn]]
                            tmp_box[turn] += 1
                            
                            hand = Hand.record(tmp_hand, piece_img[choosing[0]], signal, flag_step, flag_judged)
                            tmp_info[choosing[0]] = signal
                            object_queue.append([tmp_piece, tmp_info, tmp_hand, tmp_box])
                            undo_queue.clear()
                            selector, choosing, flag_judged, flag_step = False, None, False, False
                            if signal[0] in Const.ntoc_vert:
                                turn ^= 1
                                break
                        
                        if flag_step: break
                        if_step = Process.step_window.render(screen, signal)
                        if if_step:
                            flag_step = signal
                            break
                        return queue_holder, flag_box, param_box
                    else:   # 味方の駒か皇に当たったとき
                        if flag_step is not False:
                            msg_queue.extend(FontSet.log_msg_dict["colliding"])
                            break
                        if_step = Process.step_window.render(screen, signal)
                        if if_step:
                            flag_step = signal
                            break
                        return queue_holder, flag_box, param_box
            else:   # 駒に当たらなかったとき
                hand = Hand.record(tmp_hand, piece_img[choosing[0]], signal, flag_step, flag_judged)
                tmp_info[choosing[0]] = signal
                object_queue.append([tmp_piece, tmp_info, tmp_hand, tmp_box])
                undo_queue.clear()
                selector, choosing, flag_judged, flag_step = False, None, False, False
                if signal[0] in Const.ntoc_vert:
                    turn ^= 1
        else:
            for idx, item in enumerate(piece_img):
                if item[1].collidepoint(signal[0], signal[1]):
                    selector = True
                    choosing = (idx, item[1])
        for img_list, point in zip(tmp_piece, tmp_info):
            img_list[1].center = point
        queue_holder = [msg_queue, object_queue, undo_queue]
        flag_box = [selector, choosing, flag_judged, flag_step]
        param_box = [rate, score, turn]
        return queue_holder, flag_box, param_box

import pygame
from pygame.locals import *
from module.class_constant import *
from module.class_variable import *
from module.class_perge import *

class Render:
    @staticmethod
    def render(screen, queue_holder, flag_box, param_box):
        msg_queue, object_queue, _ = queue_holder
        piece_img, _, _, _ = object_queue[-1]
        selector, choosing, _, _ = flag_box
        rate, score, turn = param_box
        parameter_list = [str(User.point_sum-score), str(score), str(rate), FontSet.color_to_num[turn]]
        
        for piece_tuple in piece_img:
            screen.blit(piece_tuple[0], piece_tuple[1])
        
        if User.language != "pergvirle":
            for msg, msg_pos in zip(msg_queue, FontSet.log_msg_pos):
                screen.blit(msg, msg_pos)
            for param, param_pos in zip(parameter_list, FontSet.parameter_pos):
                screen.blit(FontSet.font_file.render(param, True, (0, 0, 0)), param_pos)
            for cond, cond_pos in FontSet.condition_list:
                screen.blit(cond, cond_pos)
        
            if selector:
                screen.blit(piece_img[choosing[0]][0], FontSet.image_pos)
                cur_piece_rect = choosing[1].center
                # 駒がマスにないとき
                if cur_piece_rect[0] not in Const.ntoc_vert or cur_piece_rect[1] not in Const.ntoc_horz:
                    screen.blit(FontSet.point_msg_list[0][0], FontSet.point_msg_list[0][1])
                # 駒がマスにあるとき
                else:
                    tmp = Const.ntoc_vert[cur_piece_rect[0]] + Const.ntoc_horz[cur_piece_rect[1]]
                    screen.blit(FontSet.font_file.render(tmp, True, (0, 0, 0)), FontSet.point_msg_list[0][1])
            else:
                screen.blit(FontSet.point_msg_list[1][0], FontSet.point_msg_list[1][1])
        else:
            for msg, msg_pos in zip(msg_queue, FontSet.log_msg_pos):
                screen.blit(PergeFont.wrap_up(msg, 50, 50), msg_pos)
            for param, param_pos in zip(parameter_list, FontSet.parameter_pos):
                screen.blit(FontSet.font_file.render(param, True, (0, 0, 0)), param_pos)
            for cond, cond_pos in FontSet.condition_list:
                screen.blit(PergeFont.wrap_up(cond, 50, 50), cond_pos)
            
            if selector:
                screen.blit(piece_img[choosing[0]][0], FontSet.image_pos)
                cur_piece_rect = choosing[1].center
                if cur_piece_rect[0] not in Const.ntoc_vert or cur_piece_rect[1] not in Const.ntoc_horz:
                    screen.blit(PergeFont.wrap_up(FontSet.point_msg_list[0][0], 50, 50), img_pt_pos[1])
                else:
                    tmp = Const.ntoc_vert[cur_piece_rect[0]] + Const.ntoc_horz[cur_piece_rect[1]]
                    screen.blit(PergeFont.wrap_up(tmp.lower(), 50, 50), img_pt_pos[1])
            else:
                screen.blit(PergeFont.wrap_up(pt_msg[1], 50, 50), img_pt_pos[1])
            
        return

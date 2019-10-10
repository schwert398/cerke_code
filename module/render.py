import pygame
from pygame.locals import *

from module.material import *
from module.constant import *
from module.variable import *


class Render:
    @staticmethod
    def render(screen, piece_obj_list, queue_holder, flag_box, param_box):
        msg_queue, hand_queue, _ = queue_holder
        selecting = flag_box[0]
        rate, score, turn = param_box
        parameter_list = [
            str(User.POINT_SUM-score),
            str(score),
            str(rate),
            FontSet.NUM_TO_COLOR[turn]
        ]

        for piece in piece_obj_list:
            screen.blit(piece.image, piece.rect)

        if User.LANGUAGE != "pergvirle":
            for msg, msg_pos in zip(msg_queue, FontSet.LOG_MSG_POS):
                screen.blit(msg, msg_pos)
            for cond, cond_pos in FontSet.CONDITION_LIST:
                screen.blit(cond, cond_pos)
            for param, param_pos in zip(parameter_list, FontSet.PARAMETER_POS):
                screen.blit(
                    FontSet.FONT_FILE.render(param, True, (0, 0, 0)), param_pos
                )

            # if one piece is selected (selecting is Piece in this case)
            if selecting is not False:
                choice = piece_obj_list[selecting]
                screen.blit(choice.image, FontSet.IMAGE_POS)
                piece_x, piece_y = choice.rect.center

                # if selected piece is on the board
                if piece_x in Const.VERTICAL and piece_y in Const.HORIZONTAL:
                    tmp = Const.NTOC_VERT[piece_x] + Const.NTOC_HORZ[piece_y]
                    screen.blit(
                        FontSet.FONT_FILE.render(tmp.upper(), True, (0, 0, 0)),
                        FontSet.POINT_MSG_POS
                    )
                # if selected piece is in hand
                else:
                    screen.blit(
                        FontSet.POINT_MSG_DICT["piece_space"],
                        FontSet.POINT_MSG_POS
                    )
            else:
                screen.blit(
                    FontSet.POINT_MSG_DICT["none"],
                    FontSet.POINT_MSG_POS
                )
        return

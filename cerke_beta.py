from collections import deque
import pygame
from pygame.locals import *
from class_material import *
from class_receive import *
from class_process import *
from class_constant import Constant as Cst

def main():
    pygame.init()
    pygame.font.init()
    
    # 各オブジェクトの生成
    screen = pygame.display.set_mode(Cst.window_size)
    pygame.display.set_caption("机戦")
    board = pygame.image.load("image\\field.png").convert_alpha()
    rect_board, rect_board.center = board.get_rect(), (525, 315)
    piece_space = Space.load(Cst.space_color)
    msg_font = pygame.font.SysFont("yugothicmediumyugothicuiregular", 20)
    
    # 位置・メッセージなどの箱の生成
    piece_img = Piece.load()    # 駒の画像と座標の情報
    board_info = deque([list(Cst.init_pos)], 10)    # 駒の位置情報(最新10件)
    undo_repository = list()    # undoでpopされたlistを保持(undo, redo以外のboard_infoへの操作で破棄)
    msg_queue = deque([], 5)    # メッセージログ(最新5件)

    # パラメータの生成
    rate = 1    # 点数レート
    red_score = 20          # 赤王側のスコア
    selector = False    # 選択中か
    choosing = None     # 選択しているのが何か(これはindexとRectのtupleオブジェクト)
    colliding = False   # 移動先に駒が既に存在するか
    turn = 0            # どちらの手番か(0が黒)
    
    while True:
        screen.fill(Cst.background_color)
        screen.blit(board, rect_board)
        screen.blit(piece_space, (0, 0))
        screen.blit(piece_space, (841, 0))
        
        parameter_list = [Cst.turn[turn], str(red_score), str(40-red_score), str(rate)]    # 常時表示するパラメータ(全てstrオブジェクト)
        for point, img_list in zip(board_info[-1], piece_img):
            img_list[1].center = point
        for img, rect in piece_img:
            screen.blit(img, rect)
        for msg, msg_pos in zip(msg_queue, Cst.message_pos):
            screen.blit(msg_font.render(msg, True, (0, 0, 0)), msg_pos)
        for parameter, parameter_pos in zip(parameter_list, Cst.parameter_pos):
            screen.blit(msg_font.render(parameter, True, (0, 0, 0)), parameter_pos)
        for cond, cond_pos in zip(Cst.cond_list, Cst.cond_name_pos):
            screen.blit(msg_font.render(cond, True, (0, 0, 0)), cond_pos)
        
        if selector:
            screen.blit(piece_img[choosing[0]][0], (949, 67))
            cur_piece_rect = choosing[1].center
            if cur_piece_rect[0] not in Cst.ntoc_vert or cur_piece_rect[1] not in Cst.ntoc_horz:
                screen.blit(msg_font.render("piece space", True, (0, 0, 0)), (914, 137))
            else:
                tmp = Cst.ntoc_vert[cur_piece_rect[0]] + Cst.ntoc_horz[cur_piece_rect[1]]
                screen.blit(msg_font.render(tmp, True, (0, 0, 0)), (914, 137))
        else:
            screen.blit(msg_font.render("not selecting", True, (0, 0, 0)), (914, 137))
        
        pygame.display.update()
        tmp = Receive.receive()
        if tmp is None:
            continue
        elif type(tmp) == tuple:
            ret = Process.process_tuple(tmp, board_info, piece_img, undo_repository, msg_queue, turn, selector, choosing)
            board_info, undo_repository, msg_queue, turn, selector, choosing = ret
        elif type(tmp) == str:
            ret = Process.process_str(tmp, board_info, piece_img, undo_repository, msg_queue, turn, selector, choosing, red_score, rate)
            board_info, undo_repository, msg_queue, turn, selector, choosing, red_score, rate = ret

if __name__ == "__main__":
    main()

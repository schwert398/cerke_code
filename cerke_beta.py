import json
from collections import deque
import pygame
from pygame.locals import *
from module.class_material import *
from module.class_receive import *
from module.class_process import *
from module.class_constant import *

def main():
    pygame.init()
    
    # 各オブジェクトの生成
    screen = pygame.display.set_mode(Const.window_size)
    pygame.display.set_caption("机戦")
    board = pygame.image.load("image\\field.png").convert_alpha()
    rect_board, rect_board.center = board.get_rect(), (525, 315)
    piece_space = pygame.Surface(Const.space_size)
    piece_space.fill(Const.space_color)
    setting = json.load(open("setting.json", "r"))
    
    # 言語周りの設定
    pygame.font.init()
    lang = FontSet.lang_name[setting["language"]]   # 言語を示すint
    msg_font = FontSet.font_files[lang]
    # 言語に応じた文字列と位置の情報
    condition_list, pt_msg, parameter_pos, img_pt_pos, msg_list = FontSet.load(lang)
    
    # 位置・メッセージなどの箱の生成
    piece_img = Piece.load()    # 駒の画像と座標の情報
    board_info = deque([list(Const.init_pos)], 10)    # 駒の位置情報(最新10件)
    undo_repository = list()    # undoでpopされたlistを保持(undo, redo以外のboard_infoへの操作で破棄)
    msg_queue = deque([], 5)    # メッセージログ(最新5件)

    # パラメータの生成
    rate = 1    # 点数レート
    score = 20          # 黒王側のスコア
    selector = False    # 選択中か
    choosing = None     # 選択しているのが何か(これはindexとRectのtupleオブジェクトかNoneオブジェクト)
    colliding = False   # 移動先に駒が既に存在するか
    turn = 0            # どちらの手番か(0が黒)
    
    # 各駒を初期位置へ
    for point, img_list in zip(board_info[-1], piece_img):
        img_list[1].center = point
    
    while True:
        screen.fill(Const.background_color)
        screen.blit(board, rect_board)
        screen.blit(piece_space, (0, 0))
        screen.blit(piece_space, (841, 0))
        
        parameter_list = [Const.turn[lang][turn], str(score), str(40-score), str(rate)]    # 常時表示するパラメータ(全てstrオブジェクト)
        for img, rect in piece_img:
            screen.blit(img, rect)
        for msg, msg_pos in zip(msg_queue, FontSet.message_pos):
            screen.blit(msg_font.render(msg, True, (0, 0, 0)), msg_pos)
        for param, param_pos in zip(parameter_list, parameter_pos):
            screen.blit(msg_font.render(param, True, (0, 0, 0)), param_pos)
        for cond_tuple in condition_list:
            cond, cond_pos = cond_tuple
            screen.blit(msg_font.render(cond, True, (0, 0, 0)), cond_pos)
        
        if selector:
            screen.blit(piece_img[choosing[0]][0], img_pt_pos[0])
            cur_piece_rect = choosing[1].center
            if cur_piece_rect[0] not in Const.ntoc_vert or cur_piece_rect[1] not in Const.ntoc_horz:
                screen.blit(msg_font.render(pt_msg[0], True, (0, 0, 0)), img_pt_pos[1])
            else:
                tmp = Const.ntoc_vert[cur_piece_rect[0]] + Const.ntoc_horz[cur_piece_rect[1]]
                screen.blit(msg_font.render(tmp, True, (0, 0, 0)), img_pt_pos[1])
        else:
            screen.blit(msg_font.render(pt_msg[1], True, (0, 0, 0)), img_pt_pos[1])

        # 入力の受け取りと処理
        pygame.display.update()
        tmp = Receive.receive()
        if tmp is None:
            continue
        elif type(tmp) == tuple:
            ret = Process.process_tuple(tmp, board_info, piece_img, undo_repository, lang, msg_list, msg_queue, turn, selector, choosing)
            board_info, undo_repository, msg_queue, turn, selector, choosing = ret
        elif type(tmp) == str:
            ret = Process.process_str(tmp, board_info, piece_img, undo_repository, lang, msg_list, msg_queue, turn, selector, choosing, score, rate)
            board_info, undo_repository, msg_queue, turn, selector, choosing, score, rate = ret

if __name__ == "__main__":
    main()

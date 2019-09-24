from collections import deque
import pygame
from pygame.locals import *
from module.class_material import *
from module.class_receive import *
from module.class_process import *
from module.class_constant import *
from module.class_variable import *
from module.class_render import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(Const.display_size)
    pygame.display.set_caption(FontSet.caption)
    board = pygame.image.load("image\\field.png").convert_alpha()
    rect_board, rect_board.center = board.get_rect(), (588, 315)
    piece_space = pygame.Surface(Const.space_size)
    piece_space.fill(User.space_color)
    
    # 位置・メッセージなどの箱の生成
    msg_queue = deque([], 5)    # メッセージログ(最新5件)
    piece_img = Piece.load(User.PL_color)    # 駒の画像・座標・色・向き・名前のtupleのlist
    board_info = list(Const.init_pos[User.PL_color])   # 駒の位置情報
    hand = []                   # 棋譜
    black_hand_num = 0          # 黒の手駒の数
    red_hand_num = 0            # 赤の手駒の数
    hand_num_box = [black_hand_num, red_hand_num]
    object_queue = deque([list((piece_img, board_info, hand, hand_num_box))], 10)   # 駒が動くときに更新されるもの
    undo_queue = list()    # undoでpopされたlistを保持(undo, redo以外のboard_infoへの操作で破棄)
    queue_holder = [msg_queue, object_queue, undo_queue]
    
    # フラグの生成
    selector = False    # 選択中か
    choosing = None     # 選択しているのが何か(これはindexとpiece_imgの一要素のtupleオブジェクトかNoneオブジェクト)
    flag_judged = False    # その手で裁を投げたか
    flag_step = False   # その手で踏み越えをしたか
    flag_box = [selector, choosing, flag_judged, flag_step]
    
    # パラメータの生成
    rate = 1        # 点数レート
    score = User.black_score    # 黒王側のスコア
    turn = User.first_hand      # どちらの手番か(0が黒)
    parameter_box = [rate, score, turn]

    while True:
        screen.fill(User.background_color)
        screen.blit(board, Const.board_dest)
        screen.blit(piece_space, (0, 0))
        screen.blit(piece_space, (911, 0))
        
        Render.render(screen, queue_holder, flag_box, parameter_box)
        pygame.display.update()
        
        signal = Receive.receive()
        if signal is None:
            continue
        elif type(signal) == str:
            ret = Process.proc_str(signal, screen, queue_holder, flag_box, parameter_box)
            queue_holder, flag_box, parameter_box = ret
        elif type(signal) == tuple:
            ret = Process.proc_tuple(signal, screen, queue_holder, flag_box, parameter_box)
            queue_holder, flag_box, parameter_box = ret
        
if __name__ == "__main__":
    main()

import sys
import pygame
from pygame.locals import *
from module.class_constant import Const

class Receive:
    @staticmethod
    def receive():    # 入力の受け取り・加工
        for event in pygame.event.get():
            # GUI操作
            # ウィンドウのXボタンで終了
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーボード操作
            if event.type == KEYDOWN:
                # Escで終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # spaceで選択解除 (通常モードへ)
                if event.key == K_SPACE:
                    return "space"
                # zでUndo
                if event.key == K_z:
                    return "undo"
                # qでRedo
                if event.key == K_q:
                    return "redo"
                # aで手番の変更
                if event.key == K_a:
                    return "alter"
                # rで駒の180度回転
                if event.key == K_r:
                    return "rotate"
                # iで盤面の初期化 (位置情報の末尾に初期配置を追加)
                if event.key == K_i:
                    return "initialize"
                # cで裁(標準出力に表示)
                if event.key == K_c:
                    return "ciurl"
                # p, mで点数の増減
                if event.key == K_p or event.key == K_KP_PLUS:
                    return "plus"
                if event.key == K_m or event.key == K_KP_MINUS:
                    return "minus"
                # 0, 1でレートの増減
                if event.key == K_0:
                    return "decrease"
                if event.key == K_1:
                    return "increase"
                # tで終季
                if event.key == K_t:
                    return "taxt"
                return None
            # マウス座標判定
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                x_flag, y_flag= False, False
                for v in Const.vertical:
                    if v-35 <= x <= v+35:
                        x_flag = True
                        ret_v = v
                        break
                for h in Const.horizontal:
                    if h-35 <= y <= h+35:
                        y_flag = True
                        ret_h = h
                        break
                if x_flag and y_flag:    # 重なるマス目があった場合
                    return ret_v, ret_h
                else:
                    return x, y
    

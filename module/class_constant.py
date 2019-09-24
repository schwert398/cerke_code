import pygame
from pygame.locals import *

class Const:
    # 座標の定義
    K, L, N, T, Z, X, C, M, P = 315, 385, 455, 525, 595, 665, 735, 805, 875
    A, E, I, U, O, Y, AI, AU, IA = 35, 105, 175, 245, 315, 385, 455, 525, 595
    # 縦列と横列
    vertical = (K ,L, N, T, Z, X, C, M, P)
    horizontal = (A, E, I, U, O, Y, AI, AU, IA)
    # 座標変換表
    ntoc_vert = {315:"k", 385:"l", 455:"n", 525:"t", 595:"z", 665:"x", 735:"c", 805:"m", 875:"p"}
    ntoc_horz = {35:"a", 105:"e", 175:"i", 245:"u", 315:"o", 385:"y", 455:"ai", 525:"au", 595:"ia"}
    # 色数変換
    color_to_num = {"black":0, "red":1}
    num_to_color = {0:"black", 1:"red"}
    # 向数変換
    dir_to_num = {"up":0, "down":1}
    num_to_dir = {0:"up", 1:"down"}
    # ウィンドウ・盤面・駒置の位置とサイズ
    display_size = (1191, 631)
    board_dest, board_size = (280, 0), (631, 631)
    space_dest, space_size = ((0, 0), (912, 0)), (280, 631)
    # 駒の名前・色・向き
    name = ("tam", "io", "uai", "tuk", "kua", "maun", "dau", "kaun", "gua", "kauk", "nuak")
    color = ("black", "red")
    direction = ("up", "down")
    # 初期位置
    init_pos = (
                   (
                       (Z, O),     # 皇
                       (Z, IA),    # 黒王
                       (X, IA), (T, A),    # 黒将
                       (K, AU), (P, E),    # 黒巫
                       (P, IA), (K, A),    # 黒筆
                       (M, IA), (L, A),    # 黒馬
                       (T, AU), (X, E),    # 黒虎
                       (C, IA), (N, A),    # 黒車
                       (L, AU), (M, E),    # 黒弓
                       (K, AI), (N, AI), (C, AI), (P, AI),    # 黒兵(黒王側)
                       (K, I), (N, I), (C, I), (P, I),    # 黒兵(赤王側)
                       (Z, AI),    # 黒船
                       (Z, A),     # 赤王
                       (T, IA), (X, A),    # 赤将
                       (P, AU), (K, E),    # 赤巫
                       (K, IA), (P, A),    # 赤筆
                       (L, IA), (M, A),    # 赤馬
                       (X, AU), (T, E),    # 赤虎
                       (N, IA), (C, A),    # 赤車
                       (M, AU), (L, E),    # 赤弓
                       (L, AI), (T, AI), (X, AI), (M, AI),    # 赤兵(黒王側)
                       (L, I), (T, I), (X, I), (M, I),    # 赤兵(赤王側)
                       (Z, I)   # 赤船
                   ), 
                   (
                       (Z, O),     # 皇
                       (Z, A),     # 黒王
                       (X, IA), (T, A),    # 黒将
                       (K, AU), (P, E),    # 黒巫
                       (P, IA), (K, A),    # 黒筆
                       (M, IA), (L, A),    # 黒馬
                       (T, AU), (X, E),    # 黒虎
                       (C, IA), (N, A),    # 黒車
                       (L, AU), (M, E),    # 黒弓
                       (K, AI), (N, AI), (C, AI), (P, AI),    # 黒兵(黒王側)
                       (K, I), (N, I), (C, I), (P, I),    # 黒兵(赤王側)
                       (Z, I),    # 黒船
                       (Z, IA),    # 赤王
                       (T, IA), (X, A),    # 赤将
                       (P, AU), (K, E),    # 赤巫
                       (K, IA), (P, A),    # 赤筆
                       (L, IA), (M, A),    # 赤馬
                       (X, AU), (T, E),    # 赤虎
                       (N, IA), (C, A),    # 赤車
                       (M, AU), (L, E),    # 赤弓
                       (L, AI), (T, AI), (X, AI), (M, AI),    # 赤兵(黒王側)
                       (L, I), (T, I), (X, I), (M, I),    # 赤兵(赤王側)
                       (Z, AI)   # 赤船
                   )
               )
    # 赤側駒置
    hand_pos = (
                   (
                       (245, 414),
                       (245, 344),
                       (245, 274),
                       (245, 204),
                       (245, 134),
                       (245, 64),
                       (175, 414),
                       (175, 344),
                       (175, 274),
                       (175, 204),
                       (175, 134),
                       (175, 64),
                       (105, 414),
                       (105, 344),
                       (105, 274),
                       (105, 204),
                       (105, 134),
                       (105, 64),
                       (35, 414),
                       (35, 344),
                       (35, 274),
                       (35, 204),
                       (35, 134),
                       (35, 64),
                   ),
                   ( 
                       (946, 216),
                       (946, 286),
                       (946, 356),
                       (946, 426),
                       (946, 496),
                       (946, 566),
                       (1016, 216),
                       (1016, 286),
                       (1016, 356),
                       (1016, 426),
                       (1016, 496),
                       (1016, 566),
                       (1086, 216),
                       (1086, 286),
                       (1086, 356),
                       (1086, 426),
                       (1086, 496), 
                       (1086, 566),
                       (1156, 216),
                       (1156, 286),
                       (1156, 356),
                       (1156, 426),
                       (1156, 496),
                       (1156, 566)
                   )
               )
    # 棋譜生成用
    converter_vert = {"A":"IA", "E":"AU", "I":"AI", "U":"Y", "O":"O", "Y":"U", "AI":"I", "AU":"E", "IA":"A"}
    converter_vert = {"K":"P", "L":"M", "N":"C", "T":"X", "Z":"Z", "X":"T", "C":"I", "M":"L", "P":"K"}         
    
class FontKey:
    # jsonファイルへのアクセスキー
    cond_key = ("turn", "red_score", "black_score", "rate", "choosing", "point")
    point_msg_key = ("piece_space", "none")
    log_msg_key = ("oldest", "newest", "colliding", "judged")
    window_msg_key = ("get?", "step?", "abondon?", "finish?")
    yes_no_key = ("Yes", "No")
    color_key = ("black", "red")

import pygame
from pygame.locals import *

class Constant:
    # 環境依存なもの
    # 座標の定義
    K, L, N, T, Z, X, C, M, P = 245, 315, 385, 455, 525, 595, 665, 735, 805
    A, E, I, U, O, Y, AI, AU, IA = 35, 105, 175, 245, 315, 385, 455, 525, 595
    # 縦列と横列
    vertical = (K ,L, N, T, Z, X, C, M, P)
    horizontal = (A, E, I, U, O, Y, AI, AU, IA)
    # 座標変換表
    ntoc_vert = {245:"K", 315:"L", 385:"N", 455:"T", 525:"Z", 595:"X", 665:"C", 735:"M", 805:"P"}
    ntoc_horz = {35:"A", 105:"E", 175:"I", 245:"U", 315:"O", 385:"Y", 455:"AI", 525:"AU", 595:"IA"}
    # 背景・駒置の色
    background_color = (224, 255, 255, 0)
    space_color = (255, 255, 120, 0)
    # ウィンドウ・盤面・駒置のサイズ
    window_size = (1051, 631)
    board_size = (631, 631)
    space_size = (210, 631)
    # 表示されるメッセージの位置
<<<<<<< HEAD
    message_pos = ((10, 481), (10, 511), (10, 541), (10, 571), (10, 601))
    cond_name_pos = ((851, 7), (10, 7), (851, 601), (851, 37), (851, 67), (851, 137))
    parameter_pos = ((905, 7), (111, 7), (971, 601), (915, 37))
    # 表示するメッセージ(cond_infoのみ)
    cond_list = ("turn:", "red score:", "black score:", "rate:  x","choosing:", "point:")
=======
    message_pos = ((10, 481), (10, 511), (10, 541), (10, 571), (10, 601))   # 左下のログの場所
    cond_name_pos = ((851, 7), (10, 7), (851, 601), (851, 37) ,(851, 67), (851, 137))  # cond_listの場所
    parameter_pos = ((905, 7), (111, 7), (971, 601), (915, 37))    # parameter_list(main内に記述)の場所
    # 常時表示するメッセージ
    cond_list = ("turn:", "red score:", "black score:", "rate:  x", "choosing:", "point:")
>>>>>>> e70215df14cea40b20ad1031d0876e271300adcb
    # 環境依存でないもの
    # 駒の名前・色・向き
    name = ("tam", "io", "uai", "tuk", "kua", "maun", "dau", "kaun", "gua", "kauk", "nuak")
    color = ("b", "r")
    direction = ("up", "down")
    turn = ("black", "red")
    # 初期位置
    init_pos = ((Z, O),     # 皇
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
    (Z, I))    # 赤船 
    # 

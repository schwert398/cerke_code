import pygame
from pygame.locals import *

class Constant:
    # 座標の定義
    K, L, N, T, Z, X, C, M, P = 245, 315, 385, 455, 525, 595, 665, 735, 805
    A, E, I, U, O, Y, AI, AU, IA = 35, 105, 175, 245, 315, 385, 455, 525, 595
    # 縦列と横列
    vertical = (K, L, N, T, Z, X, C, M, P)
    horizontal = (A, E, I, U, O, Y, AI, AU, IA)
    # 駒の名前・色・向き
    name = ("tam", "io", "uai", "tuk", "kua", "maun", "dau", "kaun", "gua", "kauk", "nuak")
    color = ("b", "r")
    direction = ("up", "down")
    # 初期位置
    init_pos = ((Z, O),     # 皇
    (Z, IA),    # 王
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
    
    def p(self=None):
        print("called")


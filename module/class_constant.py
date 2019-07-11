import pygame
from pygame.locals import *
pygame.font.init()

class Const:
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
    # 駒の名前・色・向き
    name = ("tam", "io", "uai", "tuk", "kua", "maun", "dau", "kaun", "gua", "kauk", "nuak")
    color = ("b", "r")
    direction = ("up", "down")
    turn = (("black", "red"),
            ("deln", "ludiex"),
            )
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
    
class FontSet:
    # 言語表(インデックスに変換)
    lang_name = {"english":0, "lineparine":1, "pergvirle": 2}
    # フォントファイル一覧
    font_files = (pygame.font.SysFont("yugothicmediumyugothicuiregular", 20),
                  pygame.font.Font("font\\jietoden_liparxe.ttf", 17),
                  pygame.font.Font("font\\pek_tak.ttf", 20))
    # 表示するメッセージ(cond_nameのみ)
    condition_list = (
                    (
                        ("turn:", (851, 7)),
                        ("red score:", (10, 7)),
                        ("black score:", (851, 601)),
                        ("rate:  x", (851, 37)),
                        ("choosing:", (851, 67)), 
                        ("point:", (851, 137))
                    ),
                    (
                        ("dire:", (851, 7)),
                        ("ludiexe'd:", (10, 7)),
                        ("delne'd:", (851, 601)),
                        ("leium:", (851, 37)),
                        ("liaxe nio texten:", (851, 67)),
                        ("polto:", (851, 167)),
                    ), 
                    ()
                )
    pt_msg = (("piece space", "None"),
              ("eski tark", "iu"), 
              ("hop1 zuo1", "mun1"))
    # 表示されるメッセージの位置
    # メッセージログ
    message_pos = ((10, 481), (10, 511), (10, 541), (10, 571), (10, 601))
    # parameter_listの中身の位置(順に手番, 赤点, 黒点, レート)
    parameter_pos = (((905, 7), (111, 7), (971, 601), (915, 37)),
                     ((905, 7), (121, 7), (941, 601), (923, 37)),
                     ((905, 7), (111, 7), (971, 601), (915, 37)))
    # 選択中の駒画像と座標の表示位置
    img_pt_pos = (((949, 47), (914, 137)),
                  ((914, 92), (914, 167)),
                  ((949, 47), (914, 137)))
    
    # Processクラス用
    msg_list = (("no longer undo", "the newest condition", "colliding"), 
                ("Cene niv il", "  chajovon ny malst", "Cene niv il", "  labackon malst", "waxlarve xelvin mol", "  fal fgir(dusnij)"),
                ())
    
    @staticmethod
    def load(num):
        return (FontSet.condition_list[num],
                FontSet.pt_msg[num],
                FontSet.parameter_pos[num],
                FontSet.img_pt_pos[num],
                FontSet.msg_list[num])

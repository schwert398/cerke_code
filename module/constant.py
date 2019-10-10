import pygame
from pygame.locals import *


class Const:
    # define coord
    K, L, N, T, Z, X, C, M, P = 315, 385, 455, 525, 595, 665, 735, 805, 875
    A, E, I, U, O, Y, AI, AU, IA = 35, 105, 175, 245, 315, 385, 455, 525, 595
    VERTICAL = (K, L, N, T, Z, X, C, M, P)
    HORIZONTAL = (A, E, I, U, O, Y, AI, AU, IA)

    CONSONANT = ("K", "L", "N", "T", "Z", "X", "C", "M", "P")
    VOWEL = ("A", "E", "I", "U", "O", "Y", "AI", "AU", "IA")

    # dict assigning num to char
    NTOC_VERT = {num: char.lower() for num, char in zip(VERTICAL, CONSONANT)}
    NTOC_HORZ = {num: char.lower() for num, char in zip(HORIZONTAL, VOWEL)}

    # dict assigning char to num
    CTON_VERT = {char.lower(): num for num, char in zip(VERTICAL, CONSONANT)}
    CTON_HORZ = {char.lower(): num for num, char in zip(HORIZONTAL, VOWEL)}

    # dict assigning coord to color
    COLOR_TO_NUM = {"black": 0, "red": 1}

    # pos and siz of window, board and space
    DISPLAY_SIZE = (1191, 631)
    BOARD_DEST, BOARD_SIZE = (280, 0), (631, 631)
    SPACE_DEST, SPACE_SIZE = ((0, 0), (912, 0)), (280, 631)

    # initial pos of pieces
    """
    almost sorted in descending order by
    1. piece's number
    2. piece's color (black to red)
    """
    TAM_POS = [(Z, O), ]
    NUAK_IO_POS = (
        [(Z, I), (Z, AI), (Z, A), (Z, IA)],
        [(Z, AI), (Z, I), (Z, IA), (Z, A)]
    )
    OTHER_POS = [
        (X, IA), (T, A), (T, IA), (X, A),  # uai
        (K, AU), (P, E), (P, AU), (K, E),  # tuk
        (P, IA), (K, A), (K, IA), (P, A),  # kua
        (M, IA), (L, A), (L, IA), (M, A),  # maun
        (T, AU), (X, E), (X, AU), (T, E),  # dau
        (C, IA), (N, A), (N, IA), (C, A),  # kaun
        (L, AU), (M, E), (M, AU), (L, E),  # gua
        # kauk
        (K, AI), (N, AI), (C, AI), (P, AI), (K, I), (N, I), (C, I), (P, I),
        (L, AI), (T, AI), (X, AI), (M, AI), (L, I), (T, I), (X, I), (M, I),
    ]

    # pos of hands
    HAND_UP = [
        pygame.Rect((vert, horz), (0, 0))
        for vert in (946, 1016, 1086, 1156)
        for horz in (216, 286, 356, 426, 496, 566)
    ]
    HAND_DOWN = [
        pygame.Rect((vert, horz), (0, 0))
        for vert in (245, 175, 105, 35)
        for horz in (414, 344, 274, 204, 134, 64)
    ]
    HAND_POS = (HAND_UP, HAND_DOWN)


class FontKey:
    # dict keys of json file
    POINT_MSG_KEY = ("piece_space", "none")
    LOG_MSG_KEY = ("oldest", "newest", "colliding", "judged")
    WINDOW_MSG_KEY = ("get?", "step?", "abondon?", "finish?", "record?")
    YES_NO_KEY = ("Yes", "No")
    COLOR_KEY = ("black", "red")
    COND_KEY = (
        "turn", "red_score", "black_score", "rate", "choosing", "point"
    )

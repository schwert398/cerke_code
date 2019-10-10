import os
import json

import pygame
from pygame.locals import *

from module.constant import *

pygame.font.init()


class User:
    SETTING = json.load(open(os.getcwd() + "\\setting.json", "r"))
    LANGUAGE = SETTING["language"]
    RECORD = SETTING["record"]

    PL_COLOR = Const.COLOR_TO_NUM[SETTING["game"]["your_color"]]
    FIRST_HAND = Const.COLOR_TO_NUM[SETTING["game"]["first_hand"]]
    BLACK_SCORE = SETTING["game"]["black_score"]
    POINT_SUM = SETTING["game"]["point_sum"]

    BG_COLOR = SETTING["other"]["background_color"]
    SPACE_COLOR = SETTING["other"]["space_color"]
    HAND_COLOR = SETTING["other"]["hand_color"]


class FontSet:
    SETTING = json.load(open("lang_setup\\" + User.LANGUAGE + ".json", "r"))
    if User.LANGUAGE == "english":
        _font_path, _font_size = SETTING["FontFile"], SETTING["FontSize"]
        FONT_FILE = pygame.font.SysFont(_font_path, _font_size)
    else:
        _font_path, _font_size = SETTING["FontFile"], SETTING["FontSize"]
        FONT_FILE = pygame.font.Font("font\\" + _font_path, _font_size)

    CAPTION = SETTING["caption"]

    # list of tuples: (Surface of condition, its pos)
    CONDITION_LIST = []
    for key in FontKey.COND_KEY:
        _font_surface = FONT_FILE.render(SETTING[key][0], True, (0, 0, 0))
        _font_pos = SETTING[key][1]
        CONDITION_LIST.append((_font_surface, _font_pos))

    # dict: {key: Surface of point_msg}
    POINT_MSG_DICT = {}
    for key in FontKey.POINT_MSG_KEY:
        POINT_MSG_DICT[key] = FONT_FILE.render(SETTING[key], True, (0, 0, 0))

    # dict: {key: (Surface of window_msg, its pos)}
    WINDOW_MSG_DICT = {}
    for key in FontKey.WINDOW_MSG_KEY:
        _font_surface = FONT_FILE.render(SETTING[key][0], True, (0, 0, 0))
        _font_pos = SETTING[key][1]
        WINDOW_MSG_DICT[key] = (_font_surface, _font_pos)

    # dict: {key: (Surface of yes_no, its pos)}
    YES_NO_DICT = {}
    for key in FontKey.YES_NO_KEY:
        _font_surface = FONT_FILE.render(SETTING[key][0], True, (0, 0, 0))
        _font_pos = SETTING[key][1]
        YES_NO_DICT[key] = (_font_surface, _font_pos)

    # dict: {key: [*Surface of log_msg]}
    LOG_MSG_DICT = {}
    for key in FontKey.LOG_MSG_KEY:
        tmp_item = []
        for phrase in SETTING[key]:
            tmp_item.append(FONT_FILE.render(phrase, True, (0, 0, 0)))
        LOG_MSG_DICT[key] = tmp_item

    # dict: {num: [Surface of num(0~5)]}
    NUMBER_DICT = {}
    for num in range(6):
        NUMBER_DICT[num] = [FONT_FILE.render(str(num), True, (0, 0, 0))]

    COLOR_TO_NUM = {}
    NUM_TO_COLOR = {}
    for idx, key in enumerate(FontKey.COLOR_KEY):
        COLOR_TO_NUM[SETTING[key]] = idx
        NUM_TO_COLOR[idx] = SETTING[key]

    POINT_MSG_POS = SETTING["point_message_pos"]
    LOG_MSG_POS = SETTING["message_pos"]
    PARAMETER_POS = SETTING["parameter_pos"]
    IMAGE_POS = SETTING["image_pos"]

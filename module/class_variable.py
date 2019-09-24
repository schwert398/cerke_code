import json
import pygame
from module.class_constant import *

pygame.font.init()

class User:
    setting = json.load(open("setting.json", "r"))
    language = setting["language"]
    record = setting["record"]
    PL_color = Const.color_to_num[setting["game"]["your_color"]]
    first_hand = Const.color_to_num[setting["game"]["first_hand"]]
    black_score = setting["game"]["black_score"]
    point_sum = setting["game"]["point_sum"]
    
    background_color = setting["other"]["background_color"]
    space_color = setting["other"]["space_color"]
    hand_color = setting["other"]["hand_color"]

class FontSet:
    setting = json.load(open("lang_setup\\" + User.language + ".json", "r"))
    if User.language == "english":
        font_path, font_size = setting["FontFile"], setting["FontSize"]
        font_file = pygame.font.SysFont(font_path, font_size)
    else:
        font_path, font_size = setting["FontFile"], setting["FontSize"]
        font_file = pygame.font.Font("font\\"+ font_path, font_size)
    
    caption = setting["caption"]
    
    condition_list = [] # cond_keyの文字のsurfaceオブジェクトと位置のtupleのlist
    for key in FontKey.cond_key:
        condition_list.append((font_file.render(setting[key][0], True, (0, 0, 0)), setting[key][1]))
    point_msg_list = [] # point_msg_keyの文字のsurfaceオブジェクトと位置のtupleのlist
    for key in FontKey.point_msg_key:
        point_msg_list.append((font_file.render(setting[key][0], True, (0, 0, 0)), setting[key][1]))
    log_msg_dict = {}   # log_msg_keyの文字のsurfaceオブジェクトのlistをvalueに持つdict
    for key in FontKey.log_msg_key:
        tmp_item = []
        for i in range(len(setting[key])):
            tmp_item.append(font_file.render(setting[key][i], True, (0, 0, 0)))
        log_msg_dict[key] = tmp_item
    window_msg_list = []    # ウィンドウメッセージのsurfaceオブジェクトと位置のtupleのlist
    for key in FontKey.window_msg_key:
        window_msg_list.append((font_file.render(setting[key][0], True, (0, 0, 0)), setting[key][1]))
    yes_no_list = []
    for key in FontKey.yes_no_key:
        yes_no_list.append((font_file.render(setting[key][0], True, (0, 0, 0)), setting[key][1]))
    color_to_num = {}
    num_to_color = {}
    for idx, key in enumerate(FontKey.color_key):
        color_to_num[setting[key]] = idx
        color_to_num[idx] = setting[key]
    
    log_msg_pos = setting["massage_pos"]
    parameter_pos = setting["parameter_pos"]
    image_pos = setting["image_pos"]
    

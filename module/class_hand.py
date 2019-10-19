import json
from collections import OrderedDict
from module.class_constant import *

name_converter = {"nuak":"V", "kauk":"P", "gua":"A", "kaun":"C",
                  "dau":"T", "maun":"H", "kua":"O", "tuk":"S",
                  "uai":"G", "io":"K", "tam":"M"}

output_dict = OrderedDict()
output_file = open("note_test.json", "w", encoding="utf-8")

def addressor(piece):
    # if the piece is on board(return coordinate)
    if piece[1].center[0] in Const.vertical:
        ret_v = Const.ntoc_vert[piece[1].center[0]]
        ret_h = Const.ntoc_horz[piece[1].center[1]]
        return ret_v + ret_h
    # if the piece is in hand(return color)
    return piece[2][0].upper()

def namer(piece):
    return name_converter[piece[4]]

def bridger(bridge):
    ret_v = Const.ntoc_vert[bridge[0]]
    ret_h = Const.ntoc_horz[bridge[1]]
    return ret_v + ret_h

def destor(dest):
    if len(dest) == 2:
        ret_v = Const.ntoc_vert[dest[0]]
        ret_h = Const.ntoc_horz[dest[1]]
    elif len(dest) == 5:
        ret_v = Const.ntoc_vert[dest[1].center[0]]
        ret_h = Const.ntoc_horz[dest[1].center[1]]
    return ret_v + ret_h

class Hand:
    @staticmethod
    def record(hand, piece, dest, bridge, judge):
        rec = addressor(piece) + namer(piece)
        if bridge is not False: rec += bridger(bridge)
        rec += destor(dest)
        if judge is not False: rec += str(judge)
        
        hand.append(rec)
        return hand

    @staticmethod
    def output(hand):
        output_dict["note"] = hand
        output_file.write(json.dumps(output_dict, indent=4))
        output_file.close()
        return

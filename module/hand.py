import os
import json
from collections import OrderedDict

from module.constant import *
from module.material import *

PIECE_LETTER = ("V", "K", "G", "S", "O", "H", "T", "C", "A", "P")

_name_converter = {
    name: letter for name, letter in zip(Piece.NAME, PIECE_LETTER)
}
_name_converter["tam"] = "M"

_NUMBER = ("0", "1", "2", "3", "4", "5")

_output_dict = OrderedDict()


def _coordinate_encorder(point: tuple) -> str:
    try:
        ret_v = Const.NTOC_VERT[point[0]]
        ret_h = Const.NTOC_HORZ[point[1]]
        return ret_v + ret_h
    except:
        raise


def _coordinate_decorder(hand: str) -> tuple:
    try:
        ret_v = Const.CTON_VERT[hand[0].lower()]
        ret_h = Const.CTON_HORZ[hand[1:].lower()]
        return (ret_v, ret_h)
    except:
        raise


def _addressor(piece: Piece) -> str:
    # if the piece is on board(return coordinate)
    if piece.rect.center[0] in Const.VERTICAL:
        ret = _coordinate_encorder(piece.rect.center)
        return ret
    # if the piece is in hand(return color in upper case)
    return piece.color[0].upper()


def _namer(piece: Piece) -> str:
    return _name_converter[piece.name]


def _bridger(bridge: Piece) -> str:
    try:
        ret = _coordinate_encorder(bridge.rect.center)
        return ret
    except:
        raise


def _destor(dest) -> str:
    try:
        if type(dest) == tuple:
            return _coordinate_encorder(dest)
        elif type(dest) == Piece:
            return _coordinate_encorder(dest.rect.center)
    except:
        raise


class Hand:
    @staticmethod
    def parser(hand: str):
        target_pos_index = -1
        # if get_piece func IS used in previous turn
        if "$" in hand:
            hand, target_pos_index = hand.split("$")
            target_pos_index = int(target_pos_index)
        # if get_piece func ISN'T used in previous turn
        # delete judge
        if hand[-1] in _NUMBER:
            hand = hand[:-1]
        for char in hand:
            if char in PIECE_LETTER:
                act, next_str = hand.split(char)
                break
        # if no bridge in hand
        if len(next_str) < 4:
            dest = next_str
        # if bridge in hand
        else:
            for idx in range(1, len(next_str)):
                if next_str[idx].upper() in Const.CONSONANT:
                    dest = next_str[idx:]
                    break
        return (_coordinate_decorder(act),
                _coordinate_decorder(dest),
                target_pos_index)

    @staticmethod
    def record(piece: Piece, dest, bridge: Piece, judge: int) -> str:
        try:
            rec = _addressor(piece) + _namer(piece)
            if bridge is not False:
                rec += _bridger(bridge)
            rec += _destor(dest)
            if judge is not False:
                rec += str(judge)
            return rec
        except:
            return False

    @staticmethod
    def output(hand: list):
        for idx in range(len(hand)):
            if "$" in hand[idx]:
                hand[idx], _ = hand[idx].split("$")
        hand[-1] += "=taxt"
        _output_dict["note"] = hand
        # search unused file name
        for i in range(1, 1000):
            if not os.path.isfile("cerke_record{}.json".format(i)):
                break
        _output_file = open(
            "cerke_record{}.json".format(i), "w", encoding="utf-8")
        _output_file.write(json.dumps(_output_dict, indent=4))
        _output_file.close()
        return


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

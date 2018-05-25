# coding=gbk
from pypinyin import pinyin,Style,lazy_pinyin
import Dict
import Character
from tqdm import tqdm

symbol = Character.Symbol_lst()

def similar(char1,char2): # char1,char2为拼音
    if char1[0:2] not in ['zh','ch','sh']:
        fst1 = char1[0] # 此处四行为声母韵母抽取
        end1 = char1[1:]
    else:
        fst1 = char1[0:2]
        end1 = char1[2:]
    if char2[0:2] not in ['zh','ch','sh']:
        fst2 = char2[0]
        end2 = char2[1:]
    else:
        fst2 = char2[0:2]
        end2 = char2[2:]

    # 韵母相同，声母相近
    if fst1 in Dict.similar_dict:
        if Dict.similar_dict[fst1] == fst2 and end1 == end2:
            # print("char1 char 2: 韵母相同，声母相近")
            return 0.8
    # 声母相同，韵母相近
    if end1 in Dict.similar_dict:
        if Dict.similar_dict[end1] == end2 and fst1 == fst2:
            # print("char1 char 2: 声母相同，韵母相近")
            return 0.8
    # 声母韵母均相近
    if fst1 in Dict.similar_dict and fst2 in Dict.similar_dict and end1 in Dict.similar_dict and end2 in Dict.similar_dict:
        if Dict.similar_dict[fst1] == fst2 and Dict.similar_dict[end1] == end2:
            # print("char1 char 2: 声母韵母均相近")
            return 0.6
    # print("声母韵母无联系")
    return 0

def pronunciation_index(i,j):
    if i == j:
        return 0
    else:
        tone1 = lazy_pinyin(i)[0]
        tone2 = lazy_pinyin(j)[0]
        if tone1 == tone2:
            return 1
        else:
            return similar(tone1, tone2)

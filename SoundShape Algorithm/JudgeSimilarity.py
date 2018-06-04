# coding=gbk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import Character
from tqdm import tqdm
from Cell import Cell
from Dict import TrAngle as quadDict  # 四码字典
from Dict import write_num_dict as strokeDict  # 笔画数字典
from Dict import structure_dict as structDict  # 结构字典
from Pronunciation import pronunciation_index
from config import WRITE_FACTOR, VOICE_FACTOR, QUAD_FACTOR, STROKE_NUM_FACOR, STRUCTURE_FACOT, PATH



lst = Character.Symbol_lst()
file1 = open(PATH, 'w')

# char1,char2为汉字
def getSimilarity(char1, char2):
    quadCodeOne = quadDict[char1]
    quadCodeTwo = quadDict[char2]
    strokeNumOne = int(strokeDict[char1])
    strokeNumTwo = int(strokeDict[char2])
    structure1 = structDict.setdefault(char1, None)
    structure2 = structDict.setdefault(char2, None)

    def minDistance(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a, b = len(word1) - 1, len(word2) - 1
        mem = {}

        def dist(a, b):
            if a == -1:
                return b + 1
            if b == -1:
                return a + 1
            if (a, b) in mem:
                return mem[(a, b)]
            if word1[a] == word2[b]:
                d = dist(a - 1, b - 1)
            else:
                d = min(dist(a - 1, b - 1), dist(a - 1, b), dist(a, b - 1)) + 1
            mem[(a, b)] = d
            return d

        return dist(a, b)
    if structure1 and structure2 and structure1 == structure2:
        structureIndex = 1
    else:
        structureIndex = 0

    # 定义四码相似度
    quadIndex = 1 - (minDistance(quadCodeOne, quadCodeTwo) / 4)
    # print("quadIndex: ", quadIndex)
    # 添加发音相似度
    voiceSimilarity = pronunciation_index(char1, char2)
    # print("voiceSimilarity: " + str(voiceSimilarity))

    writeNumIndex = 1 - abs((strokeNumOne - strokeNumTwo)/max(strokeNumOne, strokeNumTwo))

    shapeSimilarity = quadIndex * QUAD_FACTOR + writeNumIndex * STROKE_NUM_FACOR + structureIndex * STRUCTURE_FACOT
    generalSimilarity = shapeSimilarity * WRITE_FACTOR + voiceSimilarity * VOICE_FACTOR
    # print(char1 + " " + char2 + "  quadIndex " + str(quadIndex))
    # print(char1 + " " + char2 + "  shapeSimilarity " + str(shapeSimilarity))
    # print(char1 + " " + char2 + "  generalSimilarity " + str(generalSimilarity))
    # print("voiceSimilarity " + str(voiceSimilarity))
    # print("generalSimilarity " + str(generalSimilarity))
    # print("")
    return shapeSimilarity, voiceSimilarity, generalSimilarity




def main():
    print('形近字判断写入中...')
    data = {}
    for charOne in tqdm(lst):
        data[charOne] = []
        for charTwo in lst:
            if charOne == charTwo:
                continue
            else:
                # 设计一个加权音字形相似度算法，根据笔画数和四码相近程度来判断，若大于某一个阈值，则写入相近字文件
                shapeSimilarity, voiceSimilarity, generalSimilarity = getSimilarity(charOne, charTwo)
                if generalSimilarity >= 0.8 or shapeSimilarity >= 0.8 \
                        or (voiceSimilarity == 1 and shapeSimilarity >= 0.6):
                    data[charOne].append(Cell(charTwo, generalSimilarity=generalSimilarity, writeSimilarity=shapeSimilarity))

        data[charOne].sort(key=lambda cell : cell.generalSimilarity, reverse=True)
        characters = [getattr(cell, "character") for cell in data[charOne]]
        file1.write(charOne + ' ')
        listLen = 10
        for char in characters:
                file1.write(char)
                listLen -= 1
                if (listLen <= 0):
                    break
        file1.write("\n")
        file1.write("\n")
    file1.close()

if __name__ == '__main__':
    main()


class Cell:
    def __init__(self, character, generalSimilarity, writeSimilarity):
        self.character = character
        self.generalSimilarity = generalSimilarity
        self.writeSimilarity =writeSimilarity
        # self.voiceSimilarity = voiceSimilarity


    # def sort(self):
    #     cells = [Cell(character, generalSimilarity,writeSimilarity)
    #              for (character, generalSimilarity,writeSimilarity)
    #              in [("哎", 0.853, 0.76),("埃", 0.895, 0.76),("挨", 0.895, 0.76)]]
    #     cells.sort(key=lambda x:x.generalSimilarity,reverse=True)
    #     for element in cells:
    #         print(element.character,":",element.generalSimilarity)

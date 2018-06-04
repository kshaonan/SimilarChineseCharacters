from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


class Cell:
    def __init__(self, w2, score):
        self.w2 = w2
        self.score = score

class Record:
    def __init__(self, w1, w2, score):
        self.w1 = w1
        self.w2 = w2
        self.score = score

class Case:
    def __init__(self, w1, w2, features, label):
        self.label = label
        self.features = features
        self.w1 = w1
        self.w2 = w2

class Data:
    def __init__(self, path):
        self.cases=[]
        self.path = path

    def load_data(self):
        file = open(self.path)
        for line in file:
            strArr = line.split()
            w1 = strArr[0][0]
            w2 = strArr[0][1]
            # print(strArr)
            fea = []
            fea.append(float(strArr[1]))
            fea.append(float(strArr[2]))
            fea.append(float(strArr[3]))
            fea.append(float(strArr[4]))
            label = float(strArr[len(strArr)-1])
            if label==0.0:
                label=-1.0
            cases = Case(w1, w2, fea, label)
            self.cases.append(cases)
        file.close()

    def get_fea_data(self):
        w1 = []
        w2 = []
        feas = []
        labels = []
        for case in self.cases:
            w1.append(case.w1)
            w2.append(case.w2)
            feas.append(case.features)
            l = []
            l.append(case.label)
            labels.append(l)
        return w1, w2, feas, labels


def eval_matrix(labels, pre):
    npre = confusion_matrix(labels, pre)
    for x in npre:
        for y in x:
            print (str(y) + '\t'),
        print ('\n')
    return classification_report(labels, pre, digits=5).replace('\n\n', '\n')
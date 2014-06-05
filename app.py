__author__ = 'dquochuy'

import itertools

OPERATOR = ["+", "-", "*", "/"]


def cal_a_2(array_2):
    r = [n for n in itertools.permutations(array_2, 2)]
    result = []
    for op in OPERATOR:
        for e in r:
            result.append("(%s %s %s)" % (str(e[0]), op, str(e[1])))
    return result

def cal_a_3(array_3):
    

if __name__ == "__main__":
    a = ['AB', 3, 5, 8]
    result = itertools.permutations(a, 4)
    a = [1, 2]
    cal_a_2(a)



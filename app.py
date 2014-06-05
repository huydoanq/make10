__author__ = 'dquochuy'

import itertools

ns = {'__builtins__': None}
import re

OPERATOR = ["+", "-", "*", "/"]


def cal_a_2(array_2):
    r = list(itertools.permutations(array_2, 2))
    result = []
    for op in OPERATOR:
        for e in r:
            result.append("(%s %s %s)" % (str(e[0]), op, str(e[1])))
    return result


def cal_a_3_new(first_array, array_3, array_result):
    remain_array = [array_3[i] for i in range(0, len(array_3))
                    if i not in range(0, len(first_array))]
    if len(first_array) > 1:
        first_array = cal_a_2(first_array)
    r = []
    result = []
    if len(remain_array) > 2:
        r = cal_new(array_result, remain_array)
    elif len(remain_array) == 2:
        if len(array_result) > 0:
            result = array_result
        r = cal_a_2(remain_array)
    for op in OPERATOR:
        for e in r:
            for v in first_array:
                result.append("({0} {1} {2})".format(v, op, e))
    return result


def cal_new(result, array):
    first_array = []
    for i in range(0, len(array) / 2):
        if i == 0:
            first_array.append(array[0])
            result = cal_a_3_new(first_array, array, result)
        else:
            first_array = [array[j] for j in range(0, i + 1)]
            result = cal_a_3_new(first_array, array, result)

    return result


def get_expression(result, f):
    for t in result:
        try:
            r = eval(t, ns)
            if r == 10:
                print t
                f.write(t+ "\n")
        except Exception as e:
            continue


if __name__ == "__main__":
    try:
        flag = True
        while flag:
            print('Please input 4 number: ')
            data = raw_input()
            if re.match(r'^[0-9]+$', data):
                flag = False
        data = [n for n in data]
        list_data = list(itertools.permutations(data, 4))
        print("Results: \n")
        f = open("result.txt", "w")
        for i in list_data:
            result = []
            result = cal_new(result, i)
            get_expression(result, f)
    except Exception as e:
        print e






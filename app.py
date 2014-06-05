__author__ = 'dquochuy'

import itertools

ns = {'__builtins__': None}
import re

OPERATOR = ["+", "-", "*", "/"]


def cal_a_2(array_2):
    """
    Calculate Arrangement list with operators
    :param array_2: Array with 2 elements
    :return: String expression list
    """
    r = list(itertools.permutations(array_2, 2))
    result = []
    for op in OPERATOR:
        for e in r:
            result.append("(%s %s %s)" % (str(e[0]), op, str(e[1])))
    return result


def cal_a_3(first_array, array_3, array_result):
    remain_array = [array_3[i] for i in range(0, len(array_3))
                    if i not in range(0, len(first_array))]
    if len(first_array) == 2:
        first_array = cal_a_2(first_array)
    elif len(first_array) > 2:
        first_new = []
        first_array = cal_new(first_new, first_array)
    r = []
    result = []
    if len(remain_array) > 2:
        r = cal_new(array_result, remain_array)
    elif len(remain_array) == 2:
        if len(array_result) > 0:
            result = array_result
        r = cal_a_2(remain_array)
    elif len(remain_array) == 1:
        if len(array_result) > 0:
            result = array_result
        r = remain_array
    for op in OPERATOR:
        for e in r:
            for v in first_array:
                result.append("({0} {1} {2})".format(v, op, e))
    return result


def cal_new(result, array):
    """
    Star calculation string expression from an arrangement array
    :param result: list of string expression
    :param array: Arrangement array
    :return:
    """
    first_array = []
    for i in range(0, len(array) - 1):
        if i == 0:
            first_array.append(array[0])
        else:
            first_array = [array[j] for j in range(0, i + 1)]
        result = cal_a_3(first_array, array, result)

    return result


def get_expression(result, f):
    """
    Calculate the total of string expression
    If total is 10, print it out
    :param result: List of string expression
    :param f: log to file
    :return:
    """
    for t in set(result):
        try:
            r = eval(t, ns)
            if r == 10:
                print t
                f.write(t + "\n")
        except Exception as e:
            continue


def make_10():
    """
    Main function for make10 demo
    :return:
    """
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
        f.close()
    except Exception as e:
        print e


if __name__ == "__main__":
    make_10()





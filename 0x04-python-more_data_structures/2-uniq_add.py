#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum_uniq_nums = 0
    for i in set(my_list):
            sum_uniq_nums += i
    return sum_uniq_nums

import random


def random_list(n):
    lst = []
    for i in range(n):
        a = random.randint(1, 100)
        lst.append(a)
    return lst


def average(lst):
    total = sum(lst)
    aver = round(total / len(lst))
    return aver


def only_odd(lst):
    odd_numbers = [x for x in lst if x % 2 != 0]
    return odd_numbers


def to_string(lst):
    a = []
    a += lst
    a = str(a)
    return a, type(a)


def contains(lst, a, b):
    for i in range(len(lst) - 1):
        if lst[i] == a and lst[i + 1] == b:
            return True
    return False


def has_duplicates(lst):
    seen = []
    for a in lst:
        if a in seen:
            return True
        seen.append(a)
    return False

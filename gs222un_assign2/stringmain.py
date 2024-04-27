def concats(s, n):
    a = s * n
    return a


def count(s, x):
    c = 0
    for i in s:
        if i == x:
            c = c + 1
    return c


def reverse(s):
    a = s[::-1]
    return a


def first_last(s):
    a = s[len(s) - 1]
    b = s[0]
    return b, a


def has_two_X(s):
    a = s.count("X")
    return a == 2


def has_duplicates(s):
    return len(s) != len(set(s))

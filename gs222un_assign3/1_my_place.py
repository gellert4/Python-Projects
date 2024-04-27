import os

test = os.getcwd()


def count_directories(path):
    count = 0
    for i in os.listdir(path):
        if os.path.isdir(i):
            count += 1
    return count


def count_files(path):
    count = 0
    for i in os.listdir(path):
        if os.path.isfile(i):
            count += 1
    return count


print(f"I am righ now at: {test}")
print(f"Below me I have {count_directories(test)} directories/folders")
print(f"This directory contains {count_files(test)} files")

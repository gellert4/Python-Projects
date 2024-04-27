import os


def print_sub(dir_path, indent=""):
    print(indent + os.path.basename(dir_path))

    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            print_sub(item_path, indent + "  ")


direrct_path = os.getcwd()
print_sub(direrct_path)

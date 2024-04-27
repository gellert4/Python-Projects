import os


def list_dir(dir_path):
    return [d for d in os.listdir(dir_path)
            if os.path.isdir(os.path.join(dir_path, d))]


def list_files(dir_path):
    return [f for f in os.listdir(dir_path)
            if os.path.isfile(os.path.join(dir_path, f))]


current_dir = os.getcwd()

while True:
    print("\n1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit\n")

    choice = input("==> ")

    if choice == "1":
        direcotries = list_dir(current_dir)
        for directory in direcotries:
            print(directory)

    elif choice == "2":
        new_dir_name = input("Name of directory to enter: ")
        if new_dir_name == "..":
            current_dir = os.path.dirname(current_dir)
        else:
            new_dir_path = os.path.join(current_dir, new_dir_name)
            if os.path.isdir(new_dir_path):
                current_dir = new_dir_path
    elif choice == "3":
        files = list_files(current_dir)
        for file in files:
            print(file)
    elif choice == "4":
        print("Goodbye!")
        break

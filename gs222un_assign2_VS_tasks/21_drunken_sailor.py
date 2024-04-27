import random  # importing random function


def drunken_sailor(size, max_steps):  # define function
    x, y = 0, 0  # counter
    for i in range(max_steps):
        # Generate a random step: up, down, left, or right
        step = random.choice(["up", "down", "left", "right"])
        if step == "up":
            y += 1
        elif step == "down":
            y -= 1
        elif step == "left":
            x -= 1
        elif step == "right":
            x += 1

        # Check if it has fallen
        if abs(x) > size or abs(y) > size:
            return True  # Sailor fell into the water
    return False  # Sailor did not fall into the water


size = int(input("Enter the size: "))
max_steps = int(input("Enter the number of steps: "))
num_sailors = int(input("Enter the number of sailors: "))

sailors_fallen = 0  # counter

for i in range(num_sailors):
    if drunken_sailor(size, max_steps):
        sailors_fallen += 1

percentage_fallen = (sailors_fallen / num_sailors) * 100

# programe start printing
print(f"Out of {num_sailors} drunk sailors, {sailors_fallen} ({percentage_fallen:.2f}%) fell into the water.")

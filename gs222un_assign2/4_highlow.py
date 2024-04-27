import random
b = random.randint(1, 100)

for i in range(10):
    a = int(input("Guess " + str(i + 1) + ": "))
    if a > b:
        print("    Clue: Lower")
    elif a < b:
        print("    Clue: Higher")
    else:
        print("    Correct answer after only", i + 1, "guesses - Excellent")
        break

print("The game has ended")

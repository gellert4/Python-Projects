import random


def lotto_numbers():
    numbers = list(range(1, 36))
    random.shuffle(numbers)
    numbers = sorted(numbers[:7])
    return numbers


print("The numbers this week:")
for num in lotto_numbers():
    print(num, end=" ")
print()

import random

counts = [0] * 11
for i in range(10000):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    counts[total - 2] += 1

print("Frequency table (sum, count) for rolling two dice 10000 times")
for c, count in enumerate(counts, start=2):
    print(f"{c}\t{count}")

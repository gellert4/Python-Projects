import random


n = int(input("Enter a number of integers to be generated: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_numbers = 0
    smallest = float("inf")
    largest = float("-inf")

    print("Generated values:", end=" ")
    for i in range(n):
        rand_numb = random.randint(1, 100)
        print(rand_numb, end=" ")

        sum_numbers += rand_numb
        smallest = min(smallest, rand_numb)
        largest = max(largest, rand_numb)

    average = sum_numbers / n

print(f"\nAverage, min, and max are {round(average, 2)}, {smallest}, and {largest}")

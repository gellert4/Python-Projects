positive_numbers = []
count = 0

while True:
    a = int(input(f"Integer {len(positive_numbers) + 1}: "))
    if a < 0:
        break
    positive_numbers.append(a)
    count += 1

print(f"\nNumbers of positive integers: {count}")
print(f"Positive numbers: {positive_numbers}")

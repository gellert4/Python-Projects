n = int(input("Enter a postivie integer: "))

print("Odd numbers using for: ", end=" ")
for A in range(1, n + 1):
    if A % 2 != 0:
        print(A, end=" ")
print()

print("Odd numbers using while: ", end=" ")
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i = i + 1

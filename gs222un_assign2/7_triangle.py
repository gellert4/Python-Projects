n = int(input("Enter an odd positive integer: "))

if n % 2 == 0 or n < 1:
    print("It must be a positive odd number!")
    exit()

print("\nRigh-Angled Triangle:")
for i in range(n, 0, -1):
    spaces = (n - i)
    print(' ' * spaces + '*' * i)

print("\nIsosceles Triangle:")
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(' ' * spaces + '*' * i)

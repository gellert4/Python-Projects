A = input("Enter a chess square identifier (e.g. e5): ")
B = A[0]
C = int(A[1])

if C % 2 == 0 and B == "a" or B == "c" and C % 2 == 0 or C % 2 == 0 and B == "e" or C % 2 == 0 and B == "g":
    print(A,"is White")
else:
    print(A,"is Black")
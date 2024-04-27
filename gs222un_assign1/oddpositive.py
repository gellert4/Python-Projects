import random

A = random.randint(-10,10)
print("The generated number is:",A)

if A % 2 == 1 and A >= 1:
    print(A,"is odd and positive")
elif A % 2 == 1 and A < 0:
    print(A,"is odd and negative")
elif A % 2 == 0 and A > 0:
    print(A,"is even and positive")
elif A % 2 == 0 and A < 0:
    print(A,"is even and negative")
else:
    print(A,"is even and neither postive nor negative")
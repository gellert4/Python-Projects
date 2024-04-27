D = int(input("Provide a three digit nummber: "))

A = D//100
B = D%10
C = D//10%10

print("Sum of digits:",A + B + C)
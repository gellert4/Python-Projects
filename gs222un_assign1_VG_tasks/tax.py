A = int(input("Please provide monthly income: "))
B = int(A * 0.3)
C = int((A - 37999) * 0.05 + B)
D = int((A - 50000) * 0.05 + C)

if A < 38000:
    print("Corresponding income tax:",B)
elif 38000 <= A <= 50000:
    print("Corresponding income tax:",C)
else:
    print("Corresponding income tax:",D)
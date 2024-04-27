S = int(input("Initial savings: "))
P = int(input("Interest rate (in percentages): "))
Y = int(input("Number of years: "))

A = round(int(S + S*P/100*Y))

print("The value of your savings after",Y, "years is:", A)
a = (input("Enter a large positive integer: "))  # input positive integers
# Adding counters
Zeros = 0
Odds = 0
Evens = 0
# looping through the numbers
for i in a:
    if int(i) == 0:  # adding them to the counters
        Zeros += 1
    elif int(i) % 2 == 0:
        Evens += 1
    elif int(i) % 2 == 1:
        Odds += 1
    else:
        print("Please provide a positive integer")

# program start
print(f"Zeros: {Zeros}")
print(f"Odd: {Odds}")
print(f"Even: {Evens}")

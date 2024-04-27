def calculate_median(salaries):  # define funciton
    sorted_salaries = sorted(salaries)
    n = len(sorted_salaries)

    if n % 2 == 0:
        # If the number of salaries is even, average the two middle salaries
        middle1 = sorted_salaries[n // 2 - 1]
        middle2 = sorted_salaries[n // 2]
        median = (middle1 + middle2) // 2
    else:
        # If the number of salaries is odd, pick the middle salary
        median = sorted_salaries[n // 2]

    return median


# request input and then split it
salaries = input("Provide salaries (space-separated integers): ").split()
salaries = [int(salary) for salary in salaries]

if not salaries:
    print("No salaries provided.")
# start calculating

average = sum(salaries) // len(salaries)
gap = max(salaries) - min(salaries)
median = calculate_median(salaries)

# program start printing
print(f"Median: {median}")
print(f"Average: {average}")
print(f"Gap: {gap}")

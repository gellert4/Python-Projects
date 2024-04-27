import random  # importing random function


def pi_approximation(N):
    inside_circle = 0

    for i in range(N):  # loop through N
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if x, y is inside the circle
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    return 4 * inside_circle / N


# Define N
N_values = [100, 10000, 1000000]

# programe start, Calculate and then print values
for N in N_values:
    pi_estimate = pi_approximation(N)
    pi_error = abs(3.14159265359 - pi_estimate)  # Actual value of pi

    print(f"N = {N}, Pi Approximation = {pi_estimate}, Error = {pi_error}")

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def print_primes(num_primes):
    primes = []
    num = 2
    while len(primes) < num_primes:
        if is_prime(num):
            primes.append(num)
        num += 1

    for i in range(0, num_primes, 10):
        print(*primes[i:i+10])


num_primes = int(input("How many primes: "))
if num_primes <= 0:
    print("Please enter a positive integer.")
else:
    print_primes(num_primes)

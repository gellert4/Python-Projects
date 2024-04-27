def find_smallest_k(n):
    k = 1
    sum_of_odd_numbers = 1

    while sum_of_odd_numbers <= n:
        k += 2
        sum_of_odd_numbers += k

    return k


def find_largest_k(n):
    K = 0
    total = 0

    while total < n:
        K += 2
        total += K
    return K - 2


n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    smallest_k = find_smallest_k(n)
    largest_k = find_largest_k(n)

    print(f"\n{smallest_k} is the smallest k suck that 1+3+5+...+k > {n}")
    print(f"{largest_k} is the largest k such that 0+2+4+6+...+k < {n}")

def get_number(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


# Loop through all A, B, C, D
for A in range(1, 10):  # A != 0
    for B in range(10):
        for C in range(10):
            for D in range(1, 10):  # D != 0
                abcd = get_number(A, B, C, D)
                dcba = get_number(D, C, B, A)

                if dcba == 4 * abcd:
                    print(f"A = {A}, B = {B}, C = {C}, D = {D}")

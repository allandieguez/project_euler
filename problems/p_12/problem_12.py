from utils import factorize


def count_divisors(number):
    div_count = 1  # includes [1, number]
    _, counter = factorize(number)
    for c in counter:
        div_count *= c+1
    return div_count


def triangular_number(nth):
    return nth * (nth + 1) / 2


def find_highly_divisible_triangular_number(num_factors):
    nf = 1
    n = 0
    while nf < num_factors:
        n += 1
        if n % 2 == 0:  # even number
            nf = count_divisors(n / 2) + count_divisors(n + 1) - 1
        else:           # odd number
            nf = count_divisors((n + 1) / 2) + count_divisors(n) - 1
    # if nf > 200:
        print n, triangular_number(n), nf
    return triangular_number(n), nf


tn, nf = find_highly_divisible_triangular_number(5)
print tn, nf
print count_divisors(tn)
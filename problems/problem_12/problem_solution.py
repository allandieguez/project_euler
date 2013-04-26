from problems.problem_12.problem_statement import NUMBER_OF_DIVISORS
from problems.utils import factorize


divisor_map = {}


def count_divisors(number):
    if number in divisor_map.keys():
        return divisor_map[number]

    _, counter = factorize(number)
    if counter:
        div_count = counter[0] + 1
        for c in counter[1:]:
            div_count *= c+1
    else:
        div_count = 1

    divisor_map[number] = div_count
    return div_count


def triangular_number(nth):
    return nth * (nth + 1) / 2


def find_highly_divisible_triangular_number(num_factors):
    nf = 1
    max_nf = 1
    n = 0
    while nf < num_factors:
        n += 1
        nf = count_divisors(triangular_number(n))
        if max_nf < nf:
            max_nf = nf
            print n, triangular_number(n), nf
    return triangular_number(n), nf


def main():
    return find_highly_divisible_triangular_number(NUMBER_OF_DIVISORS)


if __name__ == "__main__":
    main()
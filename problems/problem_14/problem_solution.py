from problems.problem_14.problem_statement import MAX_START_NUM


length_map = {}


def sequence_length(number):
    seq_len = 0
    n = number
    while n > 1:
        if n in length_map.keys():
            return seq_len + length_map[n]
        if n % 2 == 0:  # even
            n /= 2
        else:      # odd
            n = (3 * n) + 1
        seq_len += 1
    length_map[number] = seq_len
    return seq_len


def main():
    max_len = 1
    start_num = 1
    for n in range(13, MAX_START_NUM):
        this_len = sequence_length(n)
        if this_len > max_len:
            max_len = this_len
            start_num = n
            print start_num, max_len
    return start_num, max_len


if __name__ == "__main__":
    main()
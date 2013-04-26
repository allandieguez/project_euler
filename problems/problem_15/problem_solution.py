from problems.problem_15.problem_statement import NUM_SQUARES


def get_num_paths(num_squares):
    return 2 ** (num_squares - 1) - 2


def main():
    print get_num_paths(NUM_SQUARES)


if __name__ == "__main__":
    main()
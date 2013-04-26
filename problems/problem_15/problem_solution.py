from problems.problem_15.problem_statement import GRID_SIZE
from math import factorial


def get_num_paths(grid_size):
    return factorial(sum(grid_size)) / (factorial(grid_size[0]) * factorial(grid_size[1]))


def main():
    print get_num_paths(GRID_SIZE)


if __name__ == "__main__":
    main()
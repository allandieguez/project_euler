from problem_statement import GRID_20x20


def largest_product(grid_matrix):
    n_rows = len(grid_matrix)
    n_cols = len(grid_matrix[0])
    prod_max = 0
    # search horizontal products
    for r in range(n_rows):
        for c in range(n_cols-3):
            prod_now = grid_matrix[r][c] * grid_matrix[r][c+1] * grid_matrix[r][c+2] * grid_matrix[r][c+3]
            if prod_now > prod_max:
                prod_max = prod_now
    # search vertical products
    for r in range(n_rows-3):
        for c in range(n_cols):
            prod_now = grid_matrix[r][c] * grid_matrix[r+1][c] * grid_matrix[r+2][c] * grid_matrix[r+3][c]
            if prod_now > prod_max:
                prod_max = prod_now
    # search left-to-right diagonal products
    for r in range(n_rows-3):
        for c in range(n_cols-3):
            prod_now = grid_matrix[r][c] * grid_matrix[r+1][c+1] * grid_matrix[r+2][c+2] * grid_matrix[r+3][c+3]
            if prod_now > prod_max:
                prod_max = prod_now
    # search right-to-left diagonal products
    for r in range(n_rows-3):
        for c in range(3, n_cols):
            prod_now = grid_matrix[r][c] * grid_matrix[r+1][c-1] * grid_matrix[r+2][c-2] * grid_matrix[r+3][c-3]
            if prod_now > prod_max:
                prod_max = prod_now
    return prod_max


def main():
    print largest_product(GRID_20x20)


if __name__ == "__main__":
    main()

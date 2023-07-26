def transpose(matrix) -> None:
    t_matrix = [[matrix[row][col] for row in range(len(matrix))]
                for col in range(len(matrix[0]))]

    print(f"Original matrix:\n{matrix}")
    print(f"Transpose matrix:\n{t_matrix}")


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    transpose(matrix)

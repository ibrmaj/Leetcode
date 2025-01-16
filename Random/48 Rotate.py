def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # transpose first
    n = 0
    i = 0
    while n < len(matrix):
        while i < len(matrix):
            matrix[i][n], matrix[n][i] = matrix[n][i], matrix[i][n]
            i += 1
        n += 1
        i = n + 1

    # flip columns
    j = 0
    m = 0
    while m < len(matrix):
        while j < ((len(matrix) - 1)/2):
            matrix[m][j], matrix[m][len(matrix) -1 - j] = matrix[m][len(matrix) -1 - j], matrix[m][j]
            j += 1
        m += 1
        j = 0


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)



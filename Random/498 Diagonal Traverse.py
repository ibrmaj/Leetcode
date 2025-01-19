def findDiagonalOrder(mat: list[list[int]]) -> list[int]:
    m = len(mat)
    n = len(mat[0])

    temp = []

    for i in range(m + n - 1):
        temp.append([])

    for i in range(m):
        for j in range(n):
            temp[i+j].append(mat[i][j])

    ans = []
    for i in range(len(temp)):
        if i % 2 == 0:
            ans.extend(temp[i][::-1])
        else:
            ans.extend(temp[i])
    return ans

print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))

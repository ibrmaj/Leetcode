def generateMatrix(n: int) -> list[list[int]]:
    ans = []
    for i in range(n):
        temp = [0] * n
        ans.append(temp)
    val = 1
    left, right = 0, len(ans[0])
    top, bottom = 0, len(ans)
    while left < right and top < bottom:
        for i in range(left, right):
            ans[top][i] = val
            val += 1
        top += 1
        for i in range(top, bottom):
            ans[i][right - 1] = val
            val += 1
        right -= 1

        for i in range(right - 1, left -1 , -1):
            ans[bottom - 1][i] = val
            val += 1
        bottom-= 1

        for i in range(bottom - 1, top - 1, -1):
            ans[i][left] = val
            val += 1
        left += 1


    return ans

print(generateMatrix(3))

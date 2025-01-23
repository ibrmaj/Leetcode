def numPairsDivisibleBy60(time: list[int]) -> int:
    checker = [0] * 60
    for t in time:
        checker[t % 60] += 1

    ans = 0

    ans += checker[0] * (checker[0] - 1) // 2

    ans += checker[30] * (checker[30] - 1) // 2

    for i in range(1, 30):
        ans += checker[i] * checker[60 - i]

    return ans

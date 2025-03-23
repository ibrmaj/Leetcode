def computeMaxNetworkThroughput(serverRates: list[int]) -> int:
    new = []
    for i in sorted(serverRates):
        new.insert(0, i)

    numservers = len(serverRates) // 3
    res = 0
    ls = []
    for i in range(numservers * 3):
        ls.append(new[i])
        if len(ls) == 3:
            ls.sort()
            res += ls[1]
            ls = []
            continue

    return res
print(computeMaxNetworkThroughput([2, 3, 4, 3, 4]))


def traderTrades(tasks: str, rewards: list[int], k: int) -> int:
    res = 0
    for i in rewards:
        res += i
    counter = {}
    for i in tasks:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for chars in counter:
        if counter[chars] > k:
            sm = 1000000
            for i in range(len(tasks)):
                if tasks[i] == chars:
                    sm = min(rewards[i], sm)
            res -= sm
    return res
print (traderTrades( "BAAAB", [1, 4, 2, 10, 3],2))






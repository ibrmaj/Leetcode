from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    mp = defaultdict(int)
    res = 0

    for num in nums:
        if not mp[num]:
            mp[num] = mp[num - 1] + mp[num + 1] + 1
            mp[num - mp[num - 1]] = mp[num]
            mp[num + mp[num + 1]] = mp[num]
            res = max(res, mp[num])
    return res

print(longestConsecutive([2,20,4,10,3,4,5]))

def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    total_s, total_t = {}, {}
    for i in range(len(s)):
        if t[i] not in total_t:
            total_t[t[i]] = 1
        if s[i] not in total_s:
            total_s[s[i]] = 1
        total_t[t[i]] += 1
        total_s[s[i]] += 1
    return total_t == total_s

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, value in enumerate(nums):
        if (target - value) in seen:
            return [seen[target - value], index]
        seen[value] = index

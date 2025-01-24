from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    # basically we look to the left of each number, cuz if  it doesnt have
    # anything to the left its a starting point and go from there
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
print(longestConsecutive([2,20,4,10,3,4,5]))

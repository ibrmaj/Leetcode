from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    # basically we look to the left of each number, cuz if  it doesnt have
    # anything to the left its a starting point and go from there
    numSet = set(nums) # as the lookup on a set is O(1)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet: #defines the start of a sequence
            length = 1
            while (num + length) in numSet: #this basically is a clever way to iterate through the set just to check if the length should increase.
                length += 1
            longest = max(length, longest)
    return longest
print(longestConsecutive([2,20,4,10,3,4,5]))

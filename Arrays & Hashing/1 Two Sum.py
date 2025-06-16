def twoSum(nums: list[int], target: int) -> list[int]:
    # How I intially interpreted the problem, Solution is O(n^2) which is very
    # inefficent i would say lol
    # i = 1
    # s = 0
    # ans = []
    # while s < len(nums):
    #     while i < len(nums):
    #         if target == nums[i] + nums[s]:
    #             ans.append(i)
    #             ans.append(s)
    #             return ans
    #         i += 1
    #     s += 1
    #     i = s + 1
    # This down below would be the most optimal solution and the way it works is
    # that we basically make an empty dict/hashmap then check to see if the
    # difference between the target and the n we are currently on is in that new
    # map, if it exists we retun the dicts value which represents the indexes. O(n)
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

print(twoSum([2,5,5,5, 1, 11], 6))






def threeSum(nums: list[int]) -> list[list[int]]:
    # The idea is that we can take one element of the list and 'fix' it then its basically the sorted 2 sum problem we have already solved 
    # we sort it because it makes it easier for the 2sum sorted approach 
    # it also helps as we are already O(n^2) so adding the nlogn for sorting does not change complexity
    ans = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and nums[i-1] == a:
            continue # we do this because we do NOT want repeats right, because if we have an i that we have already found triplets for again
            # it will just be a duplicate in our final list
        
        l = i + 1
        r = len(nums) - 1

        while l < r:
            threeSum  = a + nums[l] + nums[r]
            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                ans.append([a, nums[l], nums[r]])
                l = l + 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
                    # same duplicate idea here 
    return ans


print(threeSum([-1,0,1,2,-1,-4]))

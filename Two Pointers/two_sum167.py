def twoSum(numbers: list[int], target: int) -> list[int]:
    # we need something O(n) complexity and O(1) memory
    # still working on this
    prevMap = {}  # val : index

    for i, n in enumerate(numbers):
        if (target - n) in prevMap:
            return [prevMap[target - n] + 1, i + 1]
        prevMap[n] = i
print(twoSum([2,7,11,15], 9))



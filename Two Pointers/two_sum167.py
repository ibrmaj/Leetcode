def twoSum(numbers: list[int], target: int) -> list[int]:
    # we need something O(n) complexity and O(1) memory
    # completed, basically if you look at it since the inout is sorted we use 2
    # pointers one at the end and one at the start and if the sum is too big we
    # know that we have to lower it
    # so the right pointer goes down but if the sum is too low then we know we
    # have to go up so the left pointer goes up
    i = 0
    j = len(numbers)
    while i < j:
        if (numbers[i] + numbers[j-1] )== target:
            return [i+1, j]
        elif (numbers[i] + numbers[j-1] ) < target:
            i += 1
        elif (numbers[i] + numbers[j-1] ) > target:
            j -= 1

print(twoSum([2,7,11,15], 9))




def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    l = nums1 + nums2
    l.sort()

    if len(l) % 2 == 1:
        mid = len(l) // 2
        return float(l[mid])
    else:
        x = (len(l) // 2)
        y = x - 1
        mid = l[x] + l[y]
        return mid/2

print(findMedianSortedArrays([1,2],[3,4]))

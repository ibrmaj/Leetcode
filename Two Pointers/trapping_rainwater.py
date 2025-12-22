# ok so this is a really intersting problem that can be followed on from the
# container with most water problem. the idea is that "how much rain water" can
# we trap. the main way to do this is for each position i in the array we look
# at the maximum height on the left and the maximum height on the right - we
# then take the minimum of the 2 maximums and minus the hieght of i and then sum
# over all i.
# why this works is because <look at example image on the leetcode site> when
# we want to see how much water is trapped at each position - it is dependant on
# the max hieghts around

# 2 main algos: first one creates 3 lists to find the max heights on the left
# and right of each psoiton the subs it from the hieght-  this is O(n) but also
# O(n) of space - we can use 2 pointers to reduce the the space to linear by
# only moving the minimum of the 2 positions


def trap(height: list[int]) -> int:
    # solution with the lists - inefficient use of space
    # maxl = [0] * len(height)
    # maxr = [0] * len(height)
    #
    # for i in range(1, len(height)):
    #     maxl[i] = max(maxl[i-1], height[i-1])
    #
    # for i in range(len(height)-2, -1, -1):
    #     maxr[i] = max(maxr[i+1], height[i+1])
    #
    # ans = 0
    # for i in range(len(height)):
    #     ans += max(0, min(maxl[i], maxr[i]) - height[i])
    # return ans

    # with 2 pointers

    if not height:
        return 0

    l, r = 0, len(height)-1
    lmax, rmax = height[l], height[r]
    ans = 0

    while l<r:
        if lmax < rmax:
            l += 1
            lmax = max(lmax, height[l])
            ans += lmax - height[l]
        else:
            r -= 1
            rmax = max(rmax, height[r])
            ans += rmax - height[r]

    return ans

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

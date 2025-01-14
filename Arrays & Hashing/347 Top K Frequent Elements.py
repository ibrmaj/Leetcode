from collections import defaultdict
def topKFrequent(nums: list[int], k: int) -> list[int]:
    ans_dict = defaultdict(int)
    ans = []
    for num in nums:
        ans_dict[num] += 1
    sorted_values = sorted(ans_dict.items(), key = lambda item : item[1])
    for tup in sorted_values[-k:]:
        ans.append(tup[0])
    return ans
# the abive algo is O(nlogn) and if we use a heap we can get it down to O(klogn)
# but the most efficient is if you use a bucketsort with the index actually
# being the count and the values being a list of the numbers with that count. O(n)
# count = {}
# freq = [[] for i in range(len(nums) + 1)] this basically sets the index
#
# for num in nums:
#     count[num] = 1 + count.get(num, 0)
# for num, cnt in count.items(): as count.items() returns a tuple (key, value)
#     freq[cnt].append(num)
#
# res = []
# for i in range(len(freq) - 1, 0, -1): go backwards
#     for num in freq[i]:
#         res.append(num)
#         if len(res) == k:
#             return res

print(topKFrequent([1,1,1,2,2,3], 2))


from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list) # Accessing a key that does not exist adds it with an empty list
    for word in strs:
        counter = [0] * 26
        for l in word:
            counter[ord(l) - ord('a')] += 1 # what ord here does is that it
            # accesses the unicode of a given character and we know all the
            # lowercase letters are basically grouped together so this generates
            # 0 for a, 1 for b....
        res[tuple(counter)].append(word) # have to use tuple as its immutable
        # and dic keys have to be immutable

    return list(res.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))



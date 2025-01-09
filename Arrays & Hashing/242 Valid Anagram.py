def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    letters = 'abcdefghijklmnopqrstuvwxyz'
    sd = {}
    td = {}
    for i in letters:
        sd[i] = 0
        td[i] = 0
    for letter in s:
        sd[letter] = sd[letter] + 1
    for letter in t:
        td[letter] = td[letter] + 1
    return sd == td
print(isAnagram("rat", "car"))


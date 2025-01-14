def encode(strs: list[str]) -> str:
    ans=''
    for word in strs:
        ans += str(len(word)) + '#' + word
    return ans

def decode(s: str) -> list[str]:
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res

print(decode(encode(["neet","code","love","you"])))

def isPalindrome( s: str) -> bool:
    checker = ''
    for i in s:
        if i.isalnum():
            checker += i.lower()
    j = 0
    k = len(checker) - 1
    while j < len(checker)//2 and k > -1:
        if checker[j] != checker[k]:
            return False
        j += 1
        k -=1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))

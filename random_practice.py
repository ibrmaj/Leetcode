def isValid(s: str) -> bool:
    openings = []

    for i in s:
        if i in '([{':
            openings.append(i)
        else:
            if len(openings) == 0:
                return False

            chk = openings.pop()
            if i == ')' and chk != '(':
                return False
            elif i == ']' and chk != '[':
                return False
            elif i == '}' and chk != '{':
                return False
    if len(openings) != 0 :
        return False
    return True


print(isValid("(]"))

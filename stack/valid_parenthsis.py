def isValid(s: str) -> bool:
    # alright so the main idea here is that we need to ensure that the OPEN
    # bracket type is always closed and is always closed with the appropriate
    # close type, so what we do is simple, loop through the string and if the
    # bracket is an open we add it to the stack and if its a close type we pop
    # from the stack and check
    # if the stack is empty at the end we good

    openings = []

    for i in s:
        if i in '([{':
            openings.append(i)
        else:
            if len(openings) == 0: # we need this because it means we are
                # checking for a close when there is open so it must be False
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

print(isValid("([])"))

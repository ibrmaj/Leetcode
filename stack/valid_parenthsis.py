def isValid(s: str) -> bool:
    # alright so the main idea here is that we need to ensure that the OPEN
    # bracket type is always closed and is always closed with the appropriate
    # close type, so what we do is simple, loop through the string and if the
    # bracket is an open we add it to the stack and if its a close type we pop
    # from the stack and if they are pairs we are good and we keep going
    # but if they are not then false
    # if the stack is empty at the end we good

    opener = '([{'
    closer = ')]}'
    pairs = {'(' : ')', '[' : ']', '{' : '}'}
    stack = []

    for i in s:
        if i in opener:
            stack.append(i)
        elif len(stack) == 0 and i in closer: # starting off with a closing aint gonna cut it bud
            return False
        elif i in closer:
            x = stack.pop()
            if pairs[x] != i:
                return False
    if len(stack) > 0:
        return False
    return True

print(isValid("([])"))

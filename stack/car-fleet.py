# well wowo, what a q
# the main thing about this q is how to understand it, there is one lane the
# cars are driving on and the way it works is that if the cars reach the target
# together they are a fleet, and that the cars cannot overtake

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    pairs = []
    for i in range(len(position)):
        pairs.append((position[i], speed[i]))

    stack = []
    pairs.sort(reverse = True)
    for i in pairs:
        p, s = i
        t = (target - p) / s
        stack.append(t)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)




# so the idea is that we can obvioulsy run a nested for loop and solve this but
# to do it efficiently we use a stack, and we add the temperatures and the index
# to the stack and everytime we encounter a temp that is higher that then the head
# of the stack we pop the head and then we store our result, and the process
# essentially repeats

# so the mian algo: we check stack head to see if the temp is greater - if it is
# we pop the head and minus the indexes and store in our result array

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    results = [0] * len(temperatures)
    stack = [] # [temp, index]

    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            stacktemp, stackindex = stack.pop()
            results[stackindex] = i - stackindex
        stack.append([t,i])

    return results

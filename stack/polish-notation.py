def evalRPN(tokens: list[str]) -> int:
    stack = []
    for i in tokens:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            stack.append(-stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            stack.append((1/stack.pop()) * stack.pop())
        else:
            stack.append(int(i))
    return stack[0]


print(evalRPN(["3","-4","+"]))

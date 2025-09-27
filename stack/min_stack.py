class MinStack:
  # the idea for this one is that we want to create 2 stacks, one that actually stacks the values of interest and the other that takes care 
  # of the minimum in the stack, now the way that works is that everytime a new value is added to the stack, we run a comparison to find if that 
  # value is lower then the minimum already in the stack, if it is that value is added to the min stack, if it isnt the og min is added again,
  # its sort of a parallel stack thing going on 
    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            val = min(val, self.min[-1])
        self.min.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

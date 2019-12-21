class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, x: int) -> None:
        if len(self.stack)==0:
            self.stack.append(x)
            self.minStack.append(x)
        else:
            self.stack.append(x)
            self.minStack.append(min(x,self.minStack[-1]))# key line, use space to buy complexity

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
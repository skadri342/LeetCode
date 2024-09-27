class MinStack:

    def __init__(self):
        # Initializes a normal stack and a minStack for the minimum value to always be on top
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        # Pushes val into normal stack
        self.stack.append(val)
        # Determines the minimum value between val, and the last item of minStack array only 
        # if minStack is not empty, otherwise push val into minStack.
        val = min(val, self.minStack[-1] if self.minStack else val) 
        # Pushes val into minStack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
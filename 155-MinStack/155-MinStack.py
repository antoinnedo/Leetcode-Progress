class MinStack:

    '''
        stack
        -2 0 -1

        minStack
        -2 -2 -2
        
    '''

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # if new val is smaller than the current top element in minstack
        # =>add val to stack but add val to minstack, 
        # else add the previous value in minstack to minstack
        # if (self.stack == []) or (val<self.stack[-1]) : 
        #     self.stack.append(val)
        #     self.minStack.append(val)
        # else:
        if len(self.stack) > 0:
            self.stack.append(val)
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.stack.append(val)
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
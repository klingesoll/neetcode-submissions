class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = []

    def push(self, val: int) -> None:        
        self.stack.append(val)
        if self.miniStack:
            val = min(val, self.miniStack[-1])
        self.miniStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.miniStack.pop()


    def top(self) -> int:
        return self.stack [-1]
        

    def getMin(self) -> int:
        return self.miniStack[-1]
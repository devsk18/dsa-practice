class MinStack:

    def __init__(self):
        self.stk = []
        self.minV = math.inf

    def push(self, val: int) -> None:
        self.minV = min(self.minV, val)
        self.stk.append((val, self.minV))

    def pop(self) -> None:
        self.stk.pop()
        if self.stk:
            self.minV = self.getMin()
        else:
            self.minV = math.inf

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]

# TC : O(1)
# SC : O(N)

# Suggested: Stack/Simulation
# Key Idea: Maintaining a running minimum alongside each element in the stack to ensure O(1) retrieval time.

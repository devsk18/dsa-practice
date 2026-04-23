class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for operation in operations:
            if operation == "+":
                stack.append(stack[-2] + stack[-1])
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(operation))
        
        return sum(stack)
            

# TC : O(N)
# SC : O(N)

# Suggested: Stack/Simulation
# Key Idea: Using a stack to simulate stateful operations where recent elements influence new entries.

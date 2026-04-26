class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stk = []

        for op in tokens:
            if op == "+":
                res = stk.pop() + stk.pop()
                stk.append(res)
            elif op == "-":
                b = stk.pop()
                res = stk.pop() - b
                stk.append(res)
            elif op == "*":
                res = stk.pop() * stk.pop()
                stk.append(res)
            elif op == "/":
                b = stk.pop()
                res = stk.pop() / b
                stk.append(int(res))
            else:
                stk.append(int(op))
        
        return stk[-1]

# TC : O(N)
# SC : O(N)

# Suggested: Stack/Simulation
# Key Idea: Evaluating Reverse Polish Notation using a stack to store operands and apply operators sequentially.

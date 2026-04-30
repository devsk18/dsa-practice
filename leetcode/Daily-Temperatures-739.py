class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                stk_t, stk_i = stk.pop()
                res[stk_i] = i - stk_i
            stk.append((temp, i))

        return res

# TC : O(N)
# SC : O(N)    

# Suggested: Stack/Monotonic Stack
# Key Idea: Using a monotonic decreasing stack to efficiently find the next greater element for each item.


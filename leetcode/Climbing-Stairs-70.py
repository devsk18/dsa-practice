class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]

# TC: O(n)
# SC: O(n)

# Suggested: Dynamic Programming/Recursion
# Key Idea: Solving the problem using dynamic programming by summing the ways to reach the previous two steps.
# Consider: Can you refactor this to use constant space by storing just the last two values? (use one_prev and two_prev pointers instead of arr)

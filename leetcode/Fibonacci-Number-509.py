class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]

# TC: O(n)
# SC: O(n)

# Suggested: Dynamic Programming/Memoization
# Key Idea: Calculating Fibonacci numbers using basic recursion versus optimized dynamic programming techniques.

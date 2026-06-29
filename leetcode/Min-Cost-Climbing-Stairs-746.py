class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n < 2:
            return 0

        cur = 0
        prev = 0

        for i in range(2, n+1):
            prev, cur = cur, min(cost[i-1]+cur, cost[i-2]+prev)
        
        return cur

# TC: O(n)
# SC: O(1)

# Suggested: Dynamic Programming
# Key Idea: Using dynamic programming with state compression to find minimum cost by tracking only previous two steps.
# Consider: Can you adapt this space-optimized logic to handle variable step sizes like climbing 1, 3, or 4 steps?

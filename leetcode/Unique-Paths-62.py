class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n] * m

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                    continue
                top, left = 0, 0

                if i > 0:
                    top = dp[i-1][j]
                
                if j > 0:
                    left = dp[i][j-1]
                
                dp[i][j] = top + left
        return dp[m-1][n-1]

# TC : O(m*n)
# SC : O(m*n)

# Suggested: Dynamic Programming/Array
# Key Idea: Counting unique paths on a grid using dynamic programming or combinatorial mathematics.

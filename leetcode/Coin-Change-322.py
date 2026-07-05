class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount+1)

        for i in range(1, amount+1):
            minn = math.inf
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break        
                minn = min(minn, 1+dp[diff])
            dp[i] = minn
        
        if dp[amount] == math.inf:
            return -1
        
        return dp[amount]
        
# TC : O(n*amount) - n = len of coins
# SC : O(amount)

# Suggested: Dynamic Programming/Breadth-First Search
# Key Idea: Use dynamic programming to find the minimum number of coins for each amount up to the target.


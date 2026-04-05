class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        cur_min_price = prices[0]
        cur_max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - cur_min_price
            cur_max_profit = max(profit, cur_max_profit)
            cur_min_price = min(prices[i], cur_min_price)

        return cur_max_profit

# TC: O(N)
# SC: O(1)


# Suggested: Array/Simulation
# Key Idea: Track the minimum price seen so far while iterating to calculate maximum potential profit at each step.
# Consider: Since you nailed the linear scan, how would you adapt this logic if transaction fees were introduced for every buy or sell?

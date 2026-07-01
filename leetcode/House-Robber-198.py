class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        prev, cur = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            prev, cur = cur, max(cur, nums[i]+prev)
        
        return cur

# TC: O(n)
# SC: O(1)

# Suggested: Dynamic Programming
# Key Idea: Maximizing non-adjacent sum using dynamic programming with state compression.
# Consider: How would you adapt this logic if the houses were arranged in a circle instead of a straight line?

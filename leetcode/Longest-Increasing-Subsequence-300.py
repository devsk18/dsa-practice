class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            
        return max(dp)

# TC : O(n^2)
# SC : O(n)

# Suggested: Binary Search/Dynamic Programming
# Key Idea: Finding the longest strictly increasing subsequence using dynamic programming or binary search optimization.
# Consider: Can you optimize this to O(n log n) by maintaining a tail array and using binary search?

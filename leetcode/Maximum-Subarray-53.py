class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        curSum = 0
        
        l, r = 0, 0
        while r < len(nums) and l < len(nums):
            curSum += nums[r]

            if curSum < nums[r]:
                l = r
                curSum = nums[r]
            r += 1

            maxSum = max(curSum, maxSum)

        return maxSum

# TC : O(n)
# SC : O(1)

# Suggested: Dynamic Programming/Divide and Conquer
# Key Idea: Kadane's algorithm using dynamic programming to find maximum subarray sum in linear time.
# Consider: Since you mastered the O(n) approach, can you implement the subtle Divide and Conquer solution mentioned in the follow-up?

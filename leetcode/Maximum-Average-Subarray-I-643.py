class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = 0

        for i in range(k):
            k_sum += nums[i]

        max_avg = k_sum/k

        for i in range(k, len(nums)):
            k_sum += nums[i] - nums[i-k]
            max_avg = max(max_avg, k_sum/k)
        
        return max_avg

# TC : O(N)
# SC : O(1)

# Suggested: Sliding Window
# Key Idea: Using a fixed-size sliding window to calculate subarray sums in linear time by updating the sum incrementally.

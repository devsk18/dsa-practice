class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = csum = 0
        msum = math.inf

        for r in range(len(nums)):
            csum += nums[r]

            while csum >= target:
                msum = min(msum, (r-l+1))
                csum -= nums[l]
                l += 1
        
        return msum if msum != math.inf else 0

# TC : O(N)
# SC : O(1)

# Suggested: Sliding Window/Two Pointers
# Key Idea: Using a dynamic sliding window with two pointers to find the minimal subarray length satisfying a sum constraint in linear time.

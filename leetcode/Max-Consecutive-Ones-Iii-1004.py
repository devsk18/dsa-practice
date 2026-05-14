class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        w_max = 0
        num_zero = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1
            
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            
            win_len = r-l+1
            w_max = max(w_max, win_len)
        
        return w_max

# TC : O(n)
# SC = O(1)

# Suggested: Sliding Window/Two Pointers
# Key Idea: Maintaining a valid window by expanding the right pointer and shrinking the left when zero count exceeds k.
# Consider: Could you adapt this sliding window technique to handle scenarios where the cost of flipping varies per element?



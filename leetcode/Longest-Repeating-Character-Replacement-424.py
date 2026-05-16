class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = wmax = 0
        mem = [0] * 26
        mem_max = 0
        
        for r in range(len(s)):
            mem[ord(s[r]) - 65] += 1
            mem_max = max(mem_max, mem[ord(s[r]) - 65])
            while (r-l+1) - mem_max > k:
                mem[ord(s[l]) - 65] -= 1
                l += 1
            wmax = max(wmax, (r-l+1)) 
        
        return wmax

# TC : O(N)
# SC : O(1)

# Suggested: Sliding Window/Hash Table
# Key Idea: Using a sliding window to track the most frequent character and validating window size against k replacements.
# Consider: Can you tweak the logic to avoid recalculating the max frequency in every iteration for a slight constant-factor speedup?

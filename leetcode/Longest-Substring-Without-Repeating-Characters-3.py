class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wmax = 0
        l = 0
        mem = set()

        for r in range(len(s)):
            while s[r] in mem:
                mem.remove(s[l])
                l += 1

            wmax = max(wmax, (r-l+1))
            mem.add(s[r])
        
        return wmax

# TC : O(N)
# SC : O(N) - can be O(1) due to known common chars

# Suggested: Sliding Window/Hash Table
# Key Idea: Using a sliding window with a hash set to track unique characters and dynamically adjust boundaries.

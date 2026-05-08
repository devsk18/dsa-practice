# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n

        while lo < hi:
            mid = lo + ((hi-lo)//2)
            if (isBadVersion(mid)):
                hi = mid
            else:
                lo = mid + 1
        
        return lo

# TC : O(log N)
# SC : O(1)

# Suggested: Binary Search
# Key Idea: Finding the first true value in a sorted boolean sequence using binary search.
# Consider: How would you adapt this logic if the API had a non-negligible latency or rate limit?

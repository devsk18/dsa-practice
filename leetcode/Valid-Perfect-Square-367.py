class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num

        while lo <= hi:
            mid = (lo + hi)//2
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr > num:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False

# TC : O(log N)
# SC : O(1)

# Suggested: Binary Search
# Key Idea: Using binary search to efficiently find if an integer square root exists without built-in functions.

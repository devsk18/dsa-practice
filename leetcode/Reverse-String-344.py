class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l,r = 0, n-1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
# TC : O(N)
# SC : O(1)

# Suggested: Two Pointers/Array
# Key Idea: Reversing an array in-place using two pointers moving towards the center.
# Consider: How would you adapt this logic if you needed to reverse only a specific substring range?


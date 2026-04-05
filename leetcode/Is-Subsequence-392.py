class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        p = 0
        for c in t:
            if c == s[p]:
                p += 1
            
            if p == len(s):
                return True
        
        return False
    
# TC = O(N)
# SC = O(1)

# Suggested: Two Pointers/Greedy
# Key Idea: Iterate through t with a pointer for s to verify character order without backtracking.

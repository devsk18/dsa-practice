class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        q = columnNumber
        while q > 0: 
            q -= 1
            r = q % 26
            res.append(chr(ord('A')+r))

            q //= 26
        
        return "".join(res[::-1])

# TC : O(log 26(n))
# SC : O(log 26(n))

# Suggested: String
# Key Idea: Base-26 conversion with 1-based indexing adjustment.
# Consider: Can you implement this iteratively without reversing the result at the end?

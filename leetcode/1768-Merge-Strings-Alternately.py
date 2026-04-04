class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        r = n if n <= m else m
        res = []

        for i in range(r):
            res.append(word1[i] + word2[i])
        
        if r < n:
            res.append(word1[i+1:])
        else:
            res.append(word2[i+1:])
        
        return ''.join(res)


# TC = O(N + M)
# SC = O(N + M)

#Suggested: Two Pointers/Simulation
# Key Idea: Iterate through two strings simultaneously to merge characters alternately, then append remaining suffix.


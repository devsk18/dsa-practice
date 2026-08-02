class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        res = []
        i = j = 0

        while i<m and j<n:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)


# TC : O(m + n)
# SC : O(m + n)

# Suggested: Two Pointers/Simulation
# Key Idea: Iterate through two strings simultaneously to merge characters alternately, then append remaining suffix.

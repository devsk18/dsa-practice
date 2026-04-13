from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        count = math.inf

        for c in "balloon":
            if c not in freq:
                return 0
            count = min(count, freq[c])
        
        return min(freq['l']//2, freq['o']//2, count)

# TC : O(N)
# SC : O(1)

# Suggested: Hash Table/Counting
# Key Idea: Count character frequencies and determine the limiting factor based on required counts for 'l' and 'o'.

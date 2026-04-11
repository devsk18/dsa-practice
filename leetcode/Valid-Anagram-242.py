from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sc = Counter(s)
        # tc = Counter(t)

        return Counter(s) == Counter(t)

# TC = O(N)
# SC = O(1) - lowercase English letters - O(26)

# Suggested: Hash Table/Counting
# Key Idea: Using hash maps to count character frequencies for efficient string comparison.
# Consider: If Unicode characters enter the chat, how would your hash map strategy adapt?

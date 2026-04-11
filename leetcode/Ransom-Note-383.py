from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mem = Counter(magazine)

        for c in ransomNote:
            if mem[c] == 0:
                return False
            mem[c] -= 1
        
        return True

# TC = O(N)
# SC = O(1) -- lowercase English letters

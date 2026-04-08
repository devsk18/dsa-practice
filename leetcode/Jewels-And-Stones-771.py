class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_map = {}

        for jewel in jewels:
            jewel_map[jewel] = 1
        
        jewel_count = 0
        for stone in stones:
            if stone in jewel_map:
                jewel_count += 1
        
        return jewel_count

# TC = O(J + S)
# SC = O(J)

# Suggested: Hash Table/Enumeration
# Key Idea: Using a hash set for O(1) lookups to count character occurrences efficiently.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        mem_n1 = [0] * 26
        mem_n2 = [0] * 26

        for i in range(n1):
            mem_n1[ord(s1[i]) - 97] += 1
            mem_n2[ord(s2[i]) - 97] += 1
        
        if mem_n1 == mem_n2:
            return True

        for i in range(n1, n2):
            mem_n2[ord(s2[i]) - 97] += 1
            mem_n2[ord(s2[i-n1]) - 97] -= 1
            if mem_n1 == mem_n2:
                return True
        
        return False

# TC : O(N)
# SC : O(1) - 26 letters constant 

# Suggested: Sliding Window/Array
# Key Idea: Using a fixed-size sliding window with frequency arrays to check for string permutation inclusion efficiently.

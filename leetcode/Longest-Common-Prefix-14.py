class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        min_length = float('inf')
        for s in strs:
            min_length = min(len(s), min_length)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return strs[0][:i]

# TC: O(S) [S = total_strings * min_len]
# SC: O(1)


# Suggested: Brute-Force Search/Simulation
# Key Idea: Iterate through character positions across all strings to find the first mismatch or end of the shortest string.

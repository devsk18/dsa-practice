class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        mem = set(nums)
        longest = 0

        for num in mem:
            if num-1 not in mem:
                length = 1
                next_num = num + 1
                while next_num in mem:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        
        return longest

# TC : O(N)
# SC : O(N)

# Suggested: Hash Table/Enumeration
# Key Idea: Using a Hash Set to identify sequence starts and expanding only from those points to ensure linear time complexity.



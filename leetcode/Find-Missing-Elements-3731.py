class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start = min(nums)
        stop = max(nums)
        map = set(nums)

        res = []
        for num in range(start, stop+1):
            if num not in map:
                res.append(num)
            
        return res

# TC : O(n + m)
# SC : O(n)

# Suggested: Array/Hash Table
# Key Idea: Identify missing integers in a range defined by min and max values.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()

        for num in nums:
            if num in mem:
                return True
            mem.add(num)
        
        return False
        
# TC : O(N)
# SC : O(N)

# Suggested: Hash Table/Sorting
# Key Idea: Using a hash set to track seen elements for O(1) average-time membership checks.


""" 
n = len(nums)
m = len(set(nums))
return True if n != m else False
        
# TC : O(1)
# SC : O(1)
"""

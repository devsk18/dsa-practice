class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')

        for num in nums:
            if abs(num) <= closest:
                closest = abs(num)
        
        if closest in nums:
            return closest
        
        return -closest
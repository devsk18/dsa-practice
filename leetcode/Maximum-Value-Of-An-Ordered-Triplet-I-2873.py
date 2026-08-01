class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        maxT = 0
        maxD = 0
        maxN = 0

        for num in nums:
            maxT = max(maxT, maxD * num)
            maxD = max(maxD, maxN - num)
            maxN = max(maxN, num)
        
        return maxT

# TC : O(n)
# SC : O(1)

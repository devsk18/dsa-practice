class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = None, None
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                l = r = i
                break
        
        if l == None:
            return

        while r <= n-1:
            if nums[r] == 0:
                r += 1
            elif nums[l] == 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
                r += 1
        
# TC : O(n)
# SC : O(1)

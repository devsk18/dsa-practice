class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        
        return nums[lo]

# TC : O(Log N)
# SC : O(1)

# Suggested: Binary Search/Two Pointers
# Key Idea: Finding the minimum in a rotated sorted array using binary search by comparing mid and high elements.
# Consider: How would you adapt this logic if the array contained duplicate elements?

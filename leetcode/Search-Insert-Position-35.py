class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n-1

        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

# TC : O(log N)
# SC : O(1)

# Suggested: Binary Search/Two Pointers
# Key Idea: Utilizing binary search to find an insertion point in a sorted array with logarithmic time complexity.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        res = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        
        res.reverse()
        return res

# TC : O(N)
# SC : O(N)

# Suggested: Two Pointers/Sorting
# Key Idea: Utilizing the sorted property of input to merge squared values from both ends using two pointers for linear time complexity.
# Consider: Since you mastered this, how would you adapt this two-pointer technique if the input array was sorted but contained duplicate squares that needed specific handling?


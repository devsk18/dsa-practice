class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total > target:
                r -= 1
            else:
                l += 1

# TC : O(N)
# SC : O(1)

# Suggested: Two Pointers
# Key Idea: Leveraging the sorted property of the array to efficiently find pairs using two pointers moving from opposite ends.
# Consider: Since you nailed the linear approach, how would you adapt your logic if the input array was not sorted?

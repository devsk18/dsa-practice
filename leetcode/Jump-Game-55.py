class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        t = len(nums)-1
        for i in range(t, -1, -1):
            if nums[i] + i >= t:
                t = i 

        return t == 0

# TC : O(n)
# SC : O(1)

# Suggested: Greedy
# Key Idea: Greedy algorithm working backwards to find the leftmost reachable index.

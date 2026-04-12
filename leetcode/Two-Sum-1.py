class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in mem:
                return [i, mem[diff]]
            mem[num] = i

# TC : O(N)
# SC : O(N)

# Key Idea: Utilizing a hash table to store visited elements for O(1) complement lookup.
# Consider: Since you mastered the hash map approach, how would you solve this if the input array was already sorted?

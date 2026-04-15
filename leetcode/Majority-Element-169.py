class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            count += 1 if candidate == num else -1
                
        return candidate

# TC : O(N)
# SC : O(1)

# Suggested: Boyer–Moore Majority Vote Algorithm
# Key Idea: Finding the majority element using the Boyer-Moore Voting Algorithm by canceling out different elements.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            backtrack(i+1)
            
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res

# TC: O(n * 2^n) copying sol introduce n, backtracking makes 2^n
# SC: O(n)

# Suggested: Backtracking/Recursion
# Key Idea: Using recursion to explore inclusion and exclusion of each element to generate the power set.

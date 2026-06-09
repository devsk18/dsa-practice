class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res

# TC: O(n*n!) - n levels * n! permutation ways 
# SC: O(n)

# Suggested: Backtracking/Recursion
# Key Idea: Generating all permutations using backtracking by exploring choices and undoing them.

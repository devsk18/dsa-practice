class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(i,cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            backtrack(i+1, cur_sum)
            sol.append(candidates[i])
            backtrack(i, cur_sum + candidates[i])
            sol.pop()

        backtrack(0,0)
        return res

# TC: O(n^(t/min(c))) - target and candidates or O(n**t)
# SC: O(n)

# Suggested: Backtracking/Recursion
# Key Idea: Using backtracking to explore all unique combinations by deciding whether to include the current candidate or move to the next.
# Consider: Since you nailed the basics, how might sorting the candidates array first help you prune the search tree even earlier?

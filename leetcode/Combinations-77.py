class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            left = x
            still_need = k - len(sol)

            if left > still_need:
                backtrack(x-1)
            
            sol.append(x)
            backtrack(x-1)
            sol.pop()
            
        backtrack(n)
        return res

# TC: O(K∗Binom(N,K)) ---- k * N choose K
# SC: O(n)


# Suggested: Backtracking/Recursion
# Key Idea: Generating combinations using backtracking with pruning to optimize the search space.
# Consider: Can you spot why the pruning condition seems backwards yet the code still passes?

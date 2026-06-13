class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(open, close):
            if len(sol) == 2*n:
                res.append("".join(sol))
                return
            
            if open < n:
                sol.append('(')
                backtrack(open+1, close)
                sol.pop()

            if open > close:
                sol.append(')')
                backtrack(open, close+1)
                sol.pop()
            
        backtrack(0,0)
        return res

# TC: O(2^n) - doubling branches
# SC: O(n)

# Suggested: Backtracking/Recursion
# Key Idea: Generating valid combinations using backtracking by tracking open and close parenthesis counts.
# Consider: Since you mastered the basics, can you adapt this logic to handle invalid inputs or generate patterns with different bracket types?

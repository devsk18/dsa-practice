class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        res, sol = [], []
        n = len(digits)

        store = {
            '2': 'abc',
            '3': 'edf',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }


        def backtrack(i=0):
            if n == i:
                res.append("".join(sol))
                return
            
            for c in store[digits[i]]:
                sol.append(c)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res

# TC: O(n * 4^n)
# SC: O(n)

# Key Idea: Generate all combinations using backtracking to explore digit-letter mappings recursively.
# Consider: How would you adapt this approach if the input length grew significantly larger?

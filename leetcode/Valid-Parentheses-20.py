class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stk = []

        for i in s:
            if not stk or i not in pair:
                stk.append(i)
            elif pair[i] == stk[-1]:
                stk.pop()
            else:
                return False
        
        if len(stk) == 0:
            return True
        
        return False

# TC : O(N)
# SC : O(N)

# Suggested: Stack/Hash Table
# Key Idea: Using a stack to track open brackets and a hash map for matching pairs to ensure correct order and type.
# Consider: Since you mastered this, how would you adapt your logic to handle wildcard characters that can act as any bracket type?

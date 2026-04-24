class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            mem = set()
            for j in range(n):
                item = board[i][j]
                if item in mem:
                    return False
                elif item != '.':
                    mem.add(item)
        
        for i in range(n):
            mem = set()
            for j in range(n):
                item = board[j][i]
                if item in mem:
                    return False
                elif item != '.':
                    mem.add(item)

        boxes = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for i,j in boxes:
            mem = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    item = board[r][c]
                    if item in mem:
                        return False
                    elif item != '.':
                        mem.add(item)

        return True


# TC : O(1) - 9x9 fixed board
# SC : O(1)

# Suggested: Array/Hash Table/Simulation
# Key Idea: Validating Sudoku rules by checking rows, columns, and 3x3 sub-boxes for duplicate digits using hash sets.

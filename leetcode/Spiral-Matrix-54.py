class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i,j,k = 0,0,0
        m, n = len(matrix), len(matrix[0])
        res = []
        LEFT, RIGHT, UP, DOWN = 0,1,2,3

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1
        
        direction = RIGHT
        while len(res) != (m*n):
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                direction = DOWN
                RIGHT_WALL -= 1
                i,j = i+1, j-1
            
            elif direction == DOWN:
                while i < DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                direction = LEFT
                DOWN_WALL -= 1
                i,j = i-1, j-1

            elif direction == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                direction = UP
                LEFT_WALL += 1
                i, j = i-1, j+1

            else:
                while i > UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                direction = RIGHT
                UP_WALL += 1
                i, j = i+1, j+1
        
        return res


# TC: O(M*N)
# SC: O(1)

# Suggested: Simulation/Array
# Key Idea: Simulating matrix traversal by maintaining dynamic boundaries for rows and columns.

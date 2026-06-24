from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        mins = -1
        m = len(grid)
        n = len(grid[0])
        num_of_fresh = 0

        EMPTY, FRESH, ROTTEN = 0, 1, 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i,j))
                elif grid[i][j] == FRESH:
                    num_of_fresh += 1

        if num_of_fresh == 0:
            return 0 
        
        while q:
            q_size = len(q)
            mins+=1
            for _ in range(q_size):
                i, j = q.popleft()
                for i_dir, j_dir in [(0,1), (1,0), (-1,0), (0,-1)]:
                    new_i, new_j = i + i_dir, j + j_dir
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == FRESH:
                        grid[new_i][new_j] = ROTTEN
                        q.append((new_i, new_j))
                        num_of_fresh -= 1
            
        if num_of_fresh > 0:
            return -1

        return mins

# TC: O(m*n)
# SC: O(m*n)

# Suggested: Breadth-First Search/Queue/Simulation
# Key Idea: Using BFS to simulate multi-source propagation layer by layer to find minimum time.

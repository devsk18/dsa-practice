class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        i_num = 0

        def dfs(i,j):
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            for dir_i, dir_j in [(0,1), (1,0), (-1,0), (0,-1)]:
                new_i, new_j = dir_i + i, dir_j + j
                if 0 <= new_i < m and 0 <= new_j < n:
                    dfs(new_i, new_j)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    i_num += 1
                    dfs(i,j)
        
        return i_num

# TC: O(m*n)
# SC: O(m*n)

# Suggested: Depth-First Search/Breadth-First Search
# Key Idea: Counting connected components in a grid using Depth-First Search to sink visited land cells.

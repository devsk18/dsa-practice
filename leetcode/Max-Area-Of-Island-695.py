class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area, area = 0, [0]

        def dfs(i,j):
            if grid[i][j] != 1:
                return

            area[0] += 1
            grid[i][j] = 0

            for _i, _j in [(0,1), (1,0), (-1,0), (0,-1)]:
                n_i = i + _i
                n_j = j + _j 
                if 0 <= n_i < m and 0 <= n_j < n:
                    dfs(n_i, n_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area[0] = 0
                    dfs(i,j)
                    max_area = max(area[0], max_area)
        
        return max_area

# TC: O(m*n)
# SC: O(m*n)

# Suggested: Depth-First Search/Breadth-First Search
# Key Idea: Traverse connected components in a grid using DFS to calculate island areas and find the maximum.
# Consider: If the grid were massive, how might you adapt your DFS to avoid hitting recursion depth limits while keeping the same logic?

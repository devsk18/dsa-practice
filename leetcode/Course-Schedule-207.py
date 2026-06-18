class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisites
        for a,b in courses:
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        status = [UNVISITED] * numCourses

        def dfs(node):        
            if status[node] == VISITED: return True
            elif status[node] == VISITING: return False

            status[node] = VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            status[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

# TC: O(N+E)
# SC: O(N+E)

# Suggested: Depth-First Search/Topological Sort
# Key Idea: Detecting cycles in a directed graph using three-state DFS to determine course feasibility.

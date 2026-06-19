class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        courses = prerequisites
        res = []
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
            res.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res

# TC: O(N+E)
# SC: O(N+E)

# Suggested: Depth-First Search/Topological Sort
# Key Idea: Using DFS with three states to detect cycles and generate a topological sort order.
# Consider: How would the approach change if you used Kahn's algorithm with indegrees instead of DFS?


from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(s):
            if s == destination:
                return True
            
            for nei_node in d[s]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            
            return False

        d = defaultdict(list)

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        seen = set()
        seen.add(source)
        return dfs(source)

# TC: O(n+e)
# SC: O(n+e)

# Suggested: Depth-First Search/Breadth-First Search/Union-Find
# Key Idea: Determining connectivity in an undirected graph using Depth-First Search to traverse from source to destination.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = 0
        seen = set()
        min_heap = [(0,0)]

        while len(seen) < n:
            dis, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            cost += dis
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    dis = abs(xi-xj)+abs(yi-yj)
                    heapq.heappush(min_heap, (dis, j))
        
        return cost

# TC: O(n^2 log n) where n is the number of points
# SC: O(n^2)

# Suggested: Prim's Algorithm/Greedy
# Key Idea: Finding Minimum Spanning Tree using Prim's algorithm with Manhattan distance as edge weights.

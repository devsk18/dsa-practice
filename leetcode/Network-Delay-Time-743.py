from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v,w))

        min_times = {}
        min_heap = [(0,k)]

        while min_heap:
            time_to_v, v = heapq.heappop(min_heap)
            if v in min_times:
                continue
            
            min_times[v] = time_to_v
            for nei, time_to_nei in g[v]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_to_v + time_to_nei, nei))

        if len(min_times) == n:
            return max(min_times.values())
        
        return -1
        
# TC: O((V + E) log (V))  -- O(e log n) by leet AI
# SC: O(V + E)

# Suggested: Dijkstra's Algorithm/Heap (Priority Queue)/Shortest Path
# Key Idea: Finding single-source shortest paths in a weighted directed graph using a priority queue.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x**2 + y**2
 
        heap = []
        for x, y in points:
            d = dist(x, y)
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else:
                heapq.heappushpop(heap, (-d, x, y))
 
        return [(x, y) for d, x, y in heap]
 
# TC: O(n log k)
# SC: O(k)

# Current: Heap (Priority Queue)/Recursion
# Suggested: Quickselect/Divide and Conquer
# Key Idea: Finding the k smallest elements using a max-heap to maintain the closest points efficiently.
# Consider: Since you've nailed the heap method, how might Quickselect shave off that log k factor for even faster performance?

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            
            if y != x:
                dif = y - x
                heapq.heappush(stones,dif)
        
        return -1 * stones[0] if stones else 0

# TC : O(n log n) - visit n elements and heapify (log n) each time 
# SC : O(1)

# Suggested: Heap (Priority Queue)/Greedy/Simulation
# Key Idea: Using a max-heap to efficiently simulate the greedy process of smashing the two heaviest stones.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        res = cur = ListNode()
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        return res.next

# TC: O(n log k)
# SC: O(k)

# Suggested: Heap (Priority Queue)/Linked List/Divide and Conquer
# Key Idea: Using a min-heap to efficiently merge K sorted linked lists by always picking the smallest current head.

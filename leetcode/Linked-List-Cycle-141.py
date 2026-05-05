# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        
        return False

# TC : O(N)
# SC : O(1)

# Suggested: Two Pointers/Linked List
# Key Idea: Using slow and fast pointers to detect cycles in linear time with constant space.

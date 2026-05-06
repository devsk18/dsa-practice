# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

# TC : O(N)
# SC : O(1)

# Suggested: Two Pointers/Linked List
# Key Idea: Using fast and slow pointers to find the middle element in a single pass.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head

        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        
        return head
            

# TC : O(N)
# SC : O(1)

# Suggested: Linked List/Two Pointers
# Key Idea: Iterating through a sorted linked list to remove adjacent duplicates by adjusting pointers in place.

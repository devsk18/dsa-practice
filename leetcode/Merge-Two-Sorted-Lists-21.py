# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return head.next

    
# TC : O(N) 
# SC : O(1)

# Suggested: Linked List/Two Pointers
# Key Idea: Merging two sorted linked lists using a dummy head and two-pointer traversal.
# Consider: Since you nailed the iterative approach, how would you tackle this using recursion, and what trade-offs might that involve?

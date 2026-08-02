# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        prev = head
        while head:
            head = head.next
            prev.next = tail 
            tail = prev 
            prev = head
        return tail
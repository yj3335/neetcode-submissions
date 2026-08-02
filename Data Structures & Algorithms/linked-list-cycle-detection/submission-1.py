# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head 
        nxt = head 
        while nxt:
            cur = cur.next
            nxt = nxt.next 
            if nxt:
                nxt = nxt.next
            if nxt and cur == nxt:
                return True
        return False
            
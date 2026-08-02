# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1
        k = size - n

        if k == 0:
            head = head.next
            return head
            
        temp1, temp2 = head, head
        while k:
            k -= 1
            temp2 = temp1
            temp1 = temp1.next
        if temp1:
            temp2.next = temp1.next
        
        return head
        
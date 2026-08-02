# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_middle(self, head: ListNode) -> ListNode:
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        cur = head
        prev = None

        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        middle = self.find_middle(head)
        second_half = middle.next
        middle.next = None
        
        second_half = self.reverse_list(second_half)

        t1, t2 = head, second_half
        while t2:
            temp1, temp2 = t1.next, t2.next
            t1.next = t2
            t2.next = temp1 
            t1, t2 = temp1, temp2
        
        

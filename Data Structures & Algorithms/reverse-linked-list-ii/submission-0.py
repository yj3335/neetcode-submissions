# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, start, end):
        cur = start
        prev = None
        while cur != end:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp 
        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        mp = {}
        i = 1
        temp = head
        while temp:
            mp[i] = temp
            temp = temp.next
            i += 1
        
        leftPtrPrev = mp.get(left - 1, None)
        rightPtrNext = mp[right].next

        rightPtr = self.reverse_list(mp[left], rightPtrNext)
        mp[left].next = rightPtrNext

        if leftPtrPrev:
            leftPtrPrev.next = rightPtr
            return mp[1]
        else:
            return rightPtr
            
        



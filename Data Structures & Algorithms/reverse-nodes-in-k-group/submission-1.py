# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy #groupPrev = node before the start of current group

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: #kth = last node in the current group
                break
            groupNext = kth.next # next node after the current group 

            # cur = init to node before the group -> uska next node which is basically 
            # our group start
            # prev = should be none, but since we know we want the reversed group last node to 
            # point to the node after the group we init to groupNext
            prev, cur = groupNext, groupPrev.next
            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur 
                cur = tmp
            
            tmp = groupPrev.next # we store the node before the current group next's -> 
            # which was basically the starting node but now is last node in the list
            groupPrev.next = kth # we update the next of node before the group to point to 
            # new head of the group
            groupPrev = tmp # we jump to the last node of the current group 
            # (which is basically the first node before the loop began for the current group)
        
        return dummy.next

    def getKth(self, cur, k):
        while cur and k>0:
            cur = cur.next
            k -= 1
        return cur
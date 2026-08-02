# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        q = deque()
        q.append([root,1])
        ans = 0

        while q:
            node, dist = q.popleft()
            if not node:
                continue
            ans = max(ans, dist)
            q.append([node.left, dist+1])
            q.append([node.right, dist+1])
        
        return ans
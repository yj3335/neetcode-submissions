# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        ans = []

        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                q.append(node.left)
                q.append(node.right)
                temp.append(node.val)
            if temp:
                ans.append(temp)
        
        return ans
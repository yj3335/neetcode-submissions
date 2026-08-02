# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []

        def inorder(node):
            if not node:
                return
            
            if node.left:
                inorder(node.left)
            ans.append(node.val)
            if node.right:
                inorder(node.right)
            
            return
        
        inorder(root)
        return ans
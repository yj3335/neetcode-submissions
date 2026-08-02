# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return (left or right)
    
    def sameTree(self, s, p):
        if not s and not p:
            return True
        
        if not s or not p or s.val != p.val:
            return False
        
        left = self.sameTree(s.left, p.left)
        right = self.sameTree(s.right, p.right)

        return (left and right)
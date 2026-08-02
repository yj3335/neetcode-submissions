# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        visited = [False]
        ans = []

        while stack:
            root, v = stack.pop(), visited.pop()
            if root:
                if v:
                    ans.append(root.val)
                else:
                    stack.append(root)
                    visited.append(True)
                    stack.append(root.right)
                    visited.append(False)
                    stack.append(root.left)
                    visited.append(False)

        return ans

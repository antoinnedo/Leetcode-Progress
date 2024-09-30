# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        inf = 10**5
        if not root:
            return 0
        root_left = self.minDepth(root.left)        
        root_right = self.minDepth(root.right)

        if root_left and not root_right:
            return 1 + min(inf,root_left)

        if root_right and not root_left:
            return 1 + min(inf,root_right)

        return 1 + min(root_left, root_right)

  #O(n) because it has to check all nodes, O(h) for the height of the tree

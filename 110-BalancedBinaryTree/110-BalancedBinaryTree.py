# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #O(n) because went thru the whole tree, O(h) for the height of the tree
        result=[True]
        def height(root):
            if not root:
                return 0

            root_left = height(root.left)
            root_right = height(root.right)


            if abs(root_left - root_right)>1:
                result[0]=False
                return 0 #dont matter because result is False already

            return 1 + max(root_left, root_right) #return height to spot issue

        height(root) 

        return result[0]

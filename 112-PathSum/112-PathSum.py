# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #base case
        if  not root:
            return False

        targetSum -= root.val
        
        #return true if reaches leaf node and sum=0
        if not root.left and not root.right and targetSum == 0:
            return True

        #traversing through the tree
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        

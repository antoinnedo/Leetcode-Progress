# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #O(n) since we loop through the whole thing
        #O(logn) since it is a balance tree, and it got m nodes
        def helper(l, r):
            if l > r:
                return 

            m = (l+r)//2 #get middle index
            root = TreeNode(nums[m])
            root.left = helper(l, m-1) #move r to m-1 to get new m and set new left val
            root.right = helper(m+1, r) #move l to m+1 to get new m and set new right val

            return root

        return helper(0, len(nums)-1)

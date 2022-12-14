# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        if leftDepth==0 or rightDepth==0:
            return max(leftDepth,rightDepth)+1
        else:
            return min(leftDepth,rightDepth)+1
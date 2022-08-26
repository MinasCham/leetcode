# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Reccursive approach
    def searchDepth(self,root,depth=0):
        if root == None:
            return depth
        return max(self.searchDepth(root.left,depth+1),self.searchDepth(root.right,depth+1))
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.searchDepth(root)
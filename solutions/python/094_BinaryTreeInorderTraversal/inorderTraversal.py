# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inOrder(self,tree,root):
        if root:
            self.inOrder(tree,root.left)
            tree.append(root.val)
            self.inOrder(tree,root.right)
        return tree
        
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []
        return self.inOrder(tree,root)      
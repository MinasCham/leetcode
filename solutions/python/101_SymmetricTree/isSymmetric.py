# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Same principle as with the identical trees, but instead of checking the same leaves
# we are checking opposite ones (left/right)

class Solution(object):
    def symmetrycheck(self,tree1,tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is not None and tree2 is not None:
            return ((tree1.val==tree2.val) \
                    and self.symmetrycheck(tree1.left,tree2.right) \
                    and self.symmetrycheck(tree1.right,tree2.left)) 
        return False
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symmetrycheck(root.right,root.left)
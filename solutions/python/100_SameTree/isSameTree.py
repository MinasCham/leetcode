# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Parallel Traversal of both trees, then checking the values
# If one differs, break

class Solution(object):
    
    def identicalTrees(self,tree1,tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is not None and tree2 is not None:
            return ((tree1.val==tree2.val) \
                    and self.identicalTrees(tree1.left,tree2.left) \
                    and self.identicalTrees(tree1.right,tree2.right)) 
        return False
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.identicalTrees(p,q)
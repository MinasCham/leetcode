# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def createTree(l,r):
            if l>r:
                return None
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left=createTree(l,m-1)
            root.right=createTree(m+1,r)
            return root
        
        return createTree(0,len(nums)-1)
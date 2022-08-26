class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        # If nums2 is empty, return nums1 as is
        if n==0:
            return
        # if nums1 is empty, fill nums1 witgh values of nums2 and return
        elif m==0:
            for j in range(n):
                nums1[j]=nums2[j]
            return
        else:
            for i in range(n):
                nums1[m+i]=nums2[i]
            temp = nums1.sort()
            nums1=temp   
        return
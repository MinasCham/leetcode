class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ones =[row.count(1) for row in mat] 
        res = sorted(range(len(ones)), key=lambda k: ones[k])
        return res[:k]
        
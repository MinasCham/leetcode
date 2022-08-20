class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        tot = 0
        for i in nums:
            tot+=i
            res.append(tot)
        return res
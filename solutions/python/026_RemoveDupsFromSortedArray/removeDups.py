class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted(set(nums), key=nums.index)
        del nums[:]
        for i in temp:
            nums.append(i)
        return len(nums)
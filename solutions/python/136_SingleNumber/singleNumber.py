class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution using XOR bitwise operation (^ in python)
        xor = 0
        for num in nums:
            xor^=num
        return xor
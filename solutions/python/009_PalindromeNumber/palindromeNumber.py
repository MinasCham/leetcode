class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num2str = str(x)
        if num2str == num2str[::-1]:
            return True
        else:
            return False
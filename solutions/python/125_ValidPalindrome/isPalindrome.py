import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Faster than 99.65% of Python2 solutions
        # First, strip all non-alphanumeric characters using regex
        # Then convert all uppercase to lowercase
        # and finally, check for palindrome
        pattern = re.compile('[\W_]+')
        palindrome = pattern.sub('',s).lower()
        return palindrome==palindrome[::-1]
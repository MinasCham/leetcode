class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_b = {
                        '(': ')',
                        '{': '}',
                        '[': ']'
                        }
        stack = []
        for c in s:
            if c in dict_b.keys():
                stack.append(c)
            else:
                if not stack or dict_b[stack[-1]]!=c:
                    return False
            
                stack.pop()

        return not stack
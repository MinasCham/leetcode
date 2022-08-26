class Solution(object):
    
    # Solution based on Fibonacci numbers
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        onestep = 1
        twostep = 2
        for i in range(3,n+1,1):
            nextstep = onestep + twostep
            onestep = twostep
            twostep = nextstep
        return twostep
# Solution of finding the sqrt() using the Babylonian Method (https://www.geeksforgeeks.org/square-root-of-a-perfect-square/)
class Solution(object):
    
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x
        
        x_est = x*0.5
        e = 1
        while e>0.99:
            next_x = 0.5*(x_est + x/x_est)
            e = abs(x_est-next_x)
            x_est = next_x
        
        return int(x_est)
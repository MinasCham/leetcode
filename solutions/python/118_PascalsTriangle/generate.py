class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def ptc(n,k):
            return int((math.factorial(n)) / ((math.factorial(k)) * math.factorial(n - k)))
        
        def pascal_triangle(numRows):
            return [[ptc(row,k) for k in range(row+1)] for row in range(numRows)]
        
        ## Solution using factorial calculations
        return pascal_triangle(numRows)
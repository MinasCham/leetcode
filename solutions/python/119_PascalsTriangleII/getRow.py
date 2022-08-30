class Solution(object):
    # Same solution to problem #119 based on factorial calculation, just return the last row

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        def ptc(n,k):
            return int((math.factorial(n)) / ((math.factorial(k)) * math.factorial(n - k)))
        
        def pascal_triangle(numRows):
            return [[ptc(row,k) for k in range(row+1)] for row in range(numRows)]
        
        ## Solution using factorial calculations
        return pascal_triangle(rowIndex+1)[rowIndex] # rowIndex+1 as 0-indexing is requested
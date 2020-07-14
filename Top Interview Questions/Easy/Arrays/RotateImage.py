class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        # Transpose of the matrix
        for i in range(n):
            for j in range(i,n):
                temp = matrix[i][j]
                matrix[i][j]= matrix[j][i]
                matrix[j][i] = temp
                
        print(matrix)
        
        # Interchanging the values
        for i in range(0, n):
            for j in range(0,n/2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp
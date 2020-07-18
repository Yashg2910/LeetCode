class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        col_idx = set()
        row_idx = set()
        
        m= len(matrix)
        n= len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    col_idx.add(j)
                    row_idx.add(i)
                            
        row = [i for i in row_idx]
        col = [i for i in col_idx]
        
        row.sort()
        col.sort()
        
        print(row)
        print(col)
        
        k=0
        
        for i in range(m):
            if k<len(row) and i==row[k]:
                matrix[i] = [0]*n
                k+=1
            for j in range(len(col)):
                matrix[i][col[j]]=0
        
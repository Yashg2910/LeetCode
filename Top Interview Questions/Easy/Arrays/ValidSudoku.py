class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                if ele != '.':
                    seen += [(ele, j), (i, ele), (i//3,j//3,ele)]
        
        return len(seen) == len(set(seen))
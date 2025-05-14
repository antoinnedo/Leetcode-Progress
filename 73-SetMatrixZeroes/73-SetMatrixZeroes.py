# Last updated: 5/14/2025, 8:19:02 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        O(mn) space, time:
        set up array list to record 0s: eg: 0 at [0][0] then [0][n], [n][0] = 0, 0

        [[1,1,1],[1,0,1],[1,1,1]]

        O(m+n) space => more time:
        track col, rows with 0: col = [1,4], row = [1]
        =>set O[m][1,4] = 0, O[1][n] = 0
        
        O(max(m,n)) time:      
        """
        #O(mn) time, O(m+n) space
        col, row = [], []
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n]==0:
                    row.append(m)
                    col.append(n) 

        for m in row:
            for i in range(len(matrix[0])):
                matrix[m][i] = 0

        for n in col:
            for i in range(len(matrix)):
                matrix[i][n] = 0
        
        return

        
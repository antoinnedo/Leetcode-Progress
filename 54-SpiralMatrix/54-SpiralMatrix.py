class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        highColumn = len(matrix[0]) - 1
        highRow = len(matrix) - 1
        lowColumn = 0
        lowRow = 0
        result = []
        while highRow >= lowRow or highColumn >= lowColumn:
            if lowRow <= highRow:
                for i in range(lowColumn, highColumn + 1):
                    result.append(matrix[lowRow][i])
            
            lowRow+=1

            if lowColumn <= highColumn:   
                for i in range(lowRow, highRow + 1):
                    result.append(matrix[i][highColumn])
            
            highColumn-=1

            if lowRow <= highRow:
                for i in range(highColumn, lowColumn - 1, -1):
                    result.append(matrix[highRow][i])
                
                highRow-=1
                
            if lowColumn <= highColumn:
                for i in range(highRow, lowRow -1 , -1):
                    result.append(matrix[i][lowColumn])
            
            lowColumn+=1
            

        return result 
        '''
            01 02 03 04 05 06
            07 08 09 10 11 12
            13 14 15 16 17 18
            19 20 21 22 23 24

            1 2 3 4 5 6 | 6 rep
            12 18 24 | 3 times
            23 22 21 20 19 | 5 rep
            13 7 | 2 times
            8 9 10 11 | 4 rep
            17 | 1 times
            16 15 14 | 3 rep
            nothing left => since 17 is 1 times

            arr[m][n] loops till m=1 or n =1

            pseudo:
            columnRep = len(nums[0])
            rowRep = len(nums)

            while len(nums):
                for 0<=i < rowRep:
                //stops at nums[0][3]
                for 1<= j < colRep-1:
                //stops at nums[2][3]
                for 0>=i > rowRep-1:
                //stops at nums[2][0]
                for for 0+2>= j > colRep:
                //stops at nums[1][0]
                update columRep -=1, rowRep -=1
            
            time: O(mn)
            space: O(1)
        '''
        # columnRepetition = len(nums[0])
        # rowRepetition = len(nums)
        # currentColumn = 0
        # currentRow = 0
        # result = []
        # while columnRepetition > 0 or rowRepetition > 0:
        #     for i in range(currentColumn, columnRepetition):
        #         result.append(nums[currentRow][i])
        #     currentColumn = columnRepetition - 1
                
        #     for i in range(currentRow+1, rowRepetition):
        #         result.append(nums[i][currentColumn])
        #     currentRow = RowRepetition - 1

        #     for i in range(columnRepetition, currentColumn, -1):
        #         result.append(nums[currentRow][i])
        #     currentColumn = columnRepetition - 1

        #     for i in range(rowRepetition -1 , currentRow, -1):
        #         result.append(nums[i][currentColumn])
        #     currentRow = RowRepetition - 1   
        # return result 
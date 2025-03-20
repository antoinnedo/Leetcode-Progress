class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_sets= [set() for i in range(9)]
        row_sets= [set() for i in range(9)]
        subgrid_sets= [[set() for i in range(3)] for i in range(3)]

        for row_index in range(9):
            for column_index in range(9):
                num = board[row_index][column_index]
                if num == '.':
                    continue
                if num in row_sets[row_index]:
                    return False
                if num in column_sets[column_index]:
                    return False
                if num in subgrid_sets[row_index//3][column_index//3]:
                    return False
                row_sets[row_index].add(num)
                column_sets[column_index].add(num)
                subgrid_sets[row_index//3][column_index//3].add(num)
        
        return True
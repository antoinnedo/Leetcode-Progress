class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
      '''
      
      '''
        if m*n != len(original):
            return []

        array = []

        for i in range(m):
            row=[]
            for k in range(n):
                row.append(original[i*n+k])
            array.append(row)

        return array

'''

'''

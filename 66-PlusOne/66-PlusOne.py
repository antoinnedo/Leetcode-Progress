class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        digit i length
        if sum > 9: sum= sum-10, digit -2 +1
        '''
        def plus(index):
            
            if index < 0:
             return [1] + digits

            if digits[index]+1<10:
                digits[index]+=1
                return digits
            else:
                digits[index]=0
                return plus(index-1)
              
            
        return plus(len(digits)-1)

        '''
        Time: O(n)
        Exp: traverse through the list from the back

        Space: O(1)
        Exp: Only add 1 in the front if needed
        '''

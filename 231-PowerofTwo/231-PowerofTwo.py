class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''while n>1:
            if n%2==0:
                n=n/2
            else:
                return False
        return n==1 #O(logn), O(1)'''

        return (n>0 and n&(n-1)==0) #O(1),O(1)

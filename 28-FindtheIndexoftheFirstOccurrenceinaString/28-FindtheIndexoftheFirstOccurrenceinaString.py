class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        loop through haystakk with index i:
          loop through needle where only increase index k so we dont have to consider where i is when loop breaks:
            if haystack[i+k]=needle[i]:
              k++
            else:
              reset k
              break loop
            if finish loop:
              return index i
          i+=1
        return -1
        '''
        if len(haystack)<len(needle):
            return -1

        if  len(haystack)==len(needle):
            return 0 if needle == haystack else -1

        i, k = 0, 0
        while i<=len(haystack)-len(needle):
            while k<len(needle):
                if needle[k] == haystack[i+k]:
                    k+=1
                else:
                    k=0
                    break
                if k == len(needle):
                    return i
            i+=1

        return -1

  '''
Time: O((m-n)*n) 
Explanation: traverse through the haystack one time and traverse needle many times

Space: O(1)
Explanation: only update variables
'''

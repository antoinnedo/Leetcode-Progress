class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        len_s = len(s[len(s)-1])
        return len_s
      '''
      Time: O(n) 
      Explanation: Due to split(), access time is O(1)
      
      Space: O(n)
      Explanation: split() created a new list
      '''

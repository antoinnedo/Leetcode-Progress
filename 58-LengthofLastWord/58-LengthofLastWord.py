class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        len_s = len(s[len(s)-1])
        return len_s
                


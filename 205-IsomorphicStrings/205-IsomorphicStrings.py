#Solution 1: 
  class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictTS, dictST = {}, {}
        for i in range(len(s)):
            char1, char2 = s[i], t[i]

            if (char1 in dictTS and dictTS[char1] != char2) or ((char2 in dictST and dictST[char2] != char1)):
                return False

            dictTS[char1] = char2
            dictST[char2] = char1

        return True

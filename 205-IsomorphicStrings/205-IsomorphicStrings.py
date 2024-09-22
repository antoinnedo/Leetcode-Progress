#Solution 1: 
  # class Solution:
  #   def isIsomorphic(self, s: str, t: str) -> bool:
  #       dictTS, dictST = {}, {}
  #       for i in range(len(s)):
  #           char1, char2 = s[i], t[i]

  #           if (char1 in dictTS and dictTS[char1] != char2) or ((char2 in dictST and dictST[char2] != char1)):
  #               return False

  #           dictTS[char1] = char2
  #           dictST[char2] = char1

  #       return True

#Solution 2: 
   class Solution:
     def isIsomorphic(self, s: str, t: str) -> bool:
      dict = {}
      for i in range(len(s)):
          if s[i] not in dict:
              dict[s[i]] = t[i]
          else:
              if dict[s[i]] != t[i]:
                  return False
          
      values = dict.values() 
      return len(set(values)) == len(values)#check if the values have duplicates since 2 keys can be mapped to 1 value

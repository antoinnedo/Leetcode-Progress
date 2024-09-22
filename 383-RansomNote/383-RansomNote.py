class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for char in magazine:
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1
        for char in ransomNote:
            if char in dict:
                dict[char]-=1
            else:
                return False

            if dict[char] < 0:
                return False

        return True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for character in range(len(strs[0])):
            for word in strs:
                if character == len(word) or word[character] != strs[0][character]:
                    return result
            result += strs[0][character]
        return result

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
    
        output = ''
        words = s.split()
        output += str(words[-1])
        for i in range(len(words)-2, -1, -1):
            output += ' ' + str(words[i])

        return output

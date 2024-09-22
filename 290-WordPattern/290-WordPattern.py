class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        pattern = list(pattern)
        s = s.split()

        if len(pattern)!=len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dict:
                dict[pattern[i]] = s[i]
            else:
                if dict[pattern[i]] != s[i]:
                    return False

        return len(dict.values())==len(set(dict.values()))

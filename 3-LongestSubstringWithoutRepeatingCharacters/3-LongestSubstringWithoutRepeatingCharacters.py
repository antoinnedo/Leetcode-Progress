class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window

        #update the right pointer and add the char to set
        #if right pointer in the set (use set instead of splicing), update the left pointer
        #update the left pointer
        #return size of set

        charSet = set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res, r - l + 1)
        return res

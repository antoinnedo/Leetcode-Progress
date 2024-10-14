class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in valid.values():
                stack.append(i)
            elif i in valid.keys():
                if not stack or valid[i] != stack.pop():
                    return False

        return not stack
        
        

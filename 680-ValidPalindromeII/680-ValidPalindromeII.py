class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, left_pointer, right_pointer):
            while left_pointer < right_pointer:
                if s[left_pointer] != s[right_pointer]:
                    # Try skipping left or right character
                    skip_left = s[left_pointer + 1:right_pointer + 1]
                    skip_right = s[left_pointer:right_pointer]
                    return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
                left_pointer += 1
                right_pointer -= 1
            return True  # Return True when pointers meet or cross

        return isPalindrome(s, 0, len(s) - 1)
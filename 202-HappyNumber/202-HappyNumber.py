class Solution:
    def isHappy(self, n: int) -> bool:
        number = str(n)
        seen = set()
        current_number = n

        while current_number != 1:
            if current_number in seen:
                return False

            seen.add(current_number)

            current_number = sum(int(digit)**2 for digit in str(current_number))

        return True
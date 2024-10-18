class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        high = num
        low = 0
        while low <= high:
            mid = low + (high-low)//2
            if (mid*mid) == num:
                return True
            if (mid*mid) > num:
                high = mid - 1
            elif (mid*mid) < num:
                low = mid + 1
        return False

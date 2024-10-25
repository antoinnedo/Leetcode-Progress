class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = max(piles)

        while low <= high:
            guess = low + (high-low)//2
            hours = 0
            for pile in piles:
                hours += (pile + guess -1) // guess
            # if hours<h = > find lower, else
            if hours > h:
                low = guess + 1
            else:
                res = guess
                high = guess - 1

        return res

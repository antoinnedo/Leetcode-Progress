class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Set to track seen numbers
        seen = set()
        repeated = []

        # Iterate through nums to find duplicates
        for num in nums:
            if num in seen:
                repeated.append(num)
                # Stop if we found both repeated numbers
                if len(repeated) == 2:
                    break
            else:
                seen.add(num)

        return repeated
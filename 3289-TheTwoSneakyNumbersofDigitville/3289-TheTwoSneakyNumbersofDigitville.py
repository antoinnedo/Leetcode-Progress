class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Dictionary to track counts of numbers
        count = {}
        
        # Iterate through the nums list to populate the dictionary
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Find numbers that appear more than once
        repeated = [num for num, cnt in count.items() if cnt > 1]

        return repeated
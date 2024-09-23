class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = num ^ result

        return result

        #XOR => 0^1 = 1^0 = 1, 0^0=1^1=0
        #Time: O(n)
        

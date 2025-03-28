# Last updated: 3/28/2025, 6:00:27 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Explanation: subarray size will increase on the right, 
        if the sum is bigger than the target then right subarray exclude the left
        this allows the array to traverse the whole array
        '''
        nums_sum = 0
        left = 0
        min_length = len(nums) + 1
        for right in range(len(nums)):
            nums_sum += nums[right]

            while nums_sum >= target:
                min_length = min(min_length, right - left + 1)
                nums_sum -= nums[left]
                left += 1
        
        return min_length if min_length <= len(nums) else 0


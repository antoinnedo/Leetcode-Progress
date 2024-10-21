class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for i in range(len(nums)):
            othernum = target - nums[i]
            if othernum in hmap:
                return [hmap[othernum],i]
            hmap[nums[i]] = i

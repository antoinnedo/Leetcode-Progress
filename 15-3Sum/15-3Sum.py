#space,time: O(1), O(n^2) *excluding result space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        #sort array. O(1),O(nlogn)
        nums.sort()

        #get num1 O(1), O(n^2)
        for i in range(len(nums)):
            #skip iteration if it's the same number
            if nums[i] == nums[i-1] and i>0:
                continue
            #two pointer to get num2,3
            left = i+1
            right = len(nums)-1
            target = -nums[i]
            
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif cur_sum > target:
                    right-=1
                else:
                    left+=1
        return result

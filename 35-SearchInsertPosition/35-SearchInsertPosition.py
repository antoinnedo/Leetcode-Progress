class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        1 3 5 6 7      6
        '''

        low, high = 0, len(nums)-1

        def binarySearch(low, high):   
            if low > high:
                return low         
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                return binarySearch(mid+1, high)
            else:
                return binarySearch(low, mid-1)

        return binarySearch(low, high)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Binary search but return the last index before loop terminate
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


      '''
      Time: O(logn) 
      Explanation: The amount of loop decrease by half each time compared to n
      
      Space: O(1)
      Explanation: only updating variables
      '''

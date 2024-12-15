class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        restraint: 
        -5000 <= element <= 5000
        no repeating
        0<nums.length
        no same increment

        input: array=[3, 4, 5, 1, 2] rotated array? => how many rotations
        output: 1

        0 1 2 3 4 5 6 index

        3 4 5 6 7 1 2

        (1+6)//2 = 3 mid index=> nums[index] = mid value => 6
        (3+2)//2 = 2 actual value

        (1+6)//2 = 3 mid index=> nums[index] = mid value => 6
        (3+2)//2 = 2 actual value

        (5+6)//2 = 5 mid index => nums[5] = 1
        (1+2)//2 = 5 actual value       

        idea:
        shift back to ascending order => move each element reference => time, space
        sorted => binary search. requires sorted array, if array is not then the search cant be done properly
        identifying the broken part

        neeed:
        we need l, r
        if mid > value then move r = mid
        ese l = mid + 1

        know where the pointers are going =>


        pseudo: 
        left, right pointer, mid

        while loop:
            mid = (left+right)//2 = left + (right-left)//2
            if mid value > actual value 
                left index = mid index + 1         
            if else
                right index = mid

        return nums[leftindex]
        '''
        #implement:
        #left, right pointer, mid
        leftIndex = 0
        rightIndex = len(nums) - 1
    
        while (leftIndex<rightIndex) :
            midIndex = leftIndex + (rightIndex-leftIndex)//2
            #if mid value > right value 
            if (nums[midIndex]>nums[rightIndex]):
                leftIndex = midIndex + 1
            else:
                rightIndex = midIndex
        return nums[leftIndex]
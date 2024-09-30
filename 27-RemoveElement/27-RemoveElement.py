class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ''' 
        2 pointer:
            p1: front of array
            p2: back of array

            when p1 scan through list, if p1==val then switch p1 val with p2 val. eg: [p1], [p2] = [p2], [p1]
            -> force the match to the back, when p1==p2, return p2 as all the non-match is at the front

            2 2 3 3
        '''
        k=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k+=1

        return k

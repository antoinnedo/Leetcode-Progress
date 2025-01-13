class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count={0:0, 1:0, 2:0}
        for i in nums:
            if i in count:
                if i == 0:
                    count[0]+=1
                if i == 1:
                    count[1]+=1
                if i == 2:
                    count[2]+=1

        #count={0:2, 1:2, 2:2}
        #count.keys=[0, 1, 2]
        #nums=[]

        #loop through count.keys:
        #loop print index i times in count

        numsIndex=0
        while numsIndex<len(nums):
            # for key in count.keys():
            #     for val in count[count.keys]

            for key in count:
                for val in range(count[key]):
                    nums[numsIndex]=key
                    numsIndex+=1

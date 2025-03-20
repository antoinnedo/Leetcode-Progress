class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # 1 1 1 2 2 2 3
        #           ^
        # 1 1 2 2

        #2 pointer 1 write 1 read

        #read, write start at the same 1
        #count = 0 if =2 then count = 0
        #read keep going and if count=2, skip till new number is different from previous number.
        #write update according to read
        if not nums:
            return 0

        counter = 1
        read_pointer, write_pointer = 1, 1
        while read_pointer < len(nums):
            if nums[read_pointer] == nums[read_pointer - 1]:
                counter +=1
            else:
                counter = 1

            if counter <= 2:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

            read_pointer += 1
        
        return write_pointer
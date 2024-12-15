class Solution {
    public int findMin(int[] nums) {
        if (nums.length==1) return nums[0];
        int l = 0, r = nums.length - 1; // l = 0, r = 3
        while (l<r) {
            int midindex = l + (r-l) / 2; //midindex = 1 //midval = 14; =15
            if (nums[midindex] > nums[r]) { //nums[1] = 13 < 14 = midval ; [2]<;
                l = midindex + 1; //l = 1
            } else {
                r = midindex;
            }
        }
        return nums[l];
    }
}

/*
    1st pass 
    l=0
    r=1
    midindex=0
    midval = 1
    nums[0] = 2 > 1 => l = 1

    2nd pass
    l=0
    r=1
    midindex=0
    midval = nums[0] + nums[1] = 12 
    nums[0] = 11 < 12 => r=0

    nums[]
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int res[] = new int[2];
        for (int i = 0; i < n; i++) {
            for (int k = i+1; k < n; k++) {
                int sum = nums[i]+nums[k];
                if (sum==target) {
                    res[0]=i;
                    res[1]=k;
                    return res;
                }
            }
        }
        return res;
    }
}
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #sort then index is the number respondent to how many nums are small than your currnt
        # 8 1 2 2 3

        #sorted list: O(nlogn) + hashmap: O(n)
        # 1 2 2 3 8
        # 0 1 2 3 4

        #result
        result = []
        sorted_nums = sorted(nums)
        index_map = {}
        for index, element in enumerate(sorted_nums):
            if element not in index_map:
                index_map[element]=[]
            index_map[element].append(index)

        for num in nums:
            result.append(index_map[num][0])

        return result

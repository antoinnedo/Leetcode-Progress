class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a map O(n), O(n)
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        
        #sort map O(n),O(nlogn)
        dict_list = [(keys, values) for keys, values in dict.items()]
        dict_list.sort(key = lambda x: x[1], reverse=True)

        #return key O(n), O(k)
        res = [dict_list[i][0] for i in range(k)]
        return res
        #space, time: O(n), O(nlogn)

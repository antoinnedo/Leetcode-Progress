class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        2 7 4 1 8 1
        
        1 1 
        '''
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x - y != 0:
                heapq.heappush(stones, - abs(x-y))

        stones.append(0)        
        return abs(stones[0])

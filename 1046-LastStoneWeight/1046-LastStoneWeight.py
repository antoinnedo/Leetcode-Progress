class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        use heap: the problem requires max heap but the default is a min heap
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

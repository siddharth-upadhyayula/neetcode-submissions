class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            y = heapq.heappop(maxheap)
            x = heapq.heappop(maxheap)
            if y!=x:
                heapq.heappush(maxheap, y-x)
        return -maxheap[0] if maxheap else 0
import heapq;
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distance = 0
        minheap = []
        heapq.heapify(minheap)
        for i in range(len(points)):

            distance = math.sqrt(math.pow((0-points[i][0]),2) + math.pow((0-points[i][1]),2))

            heapq.heappush(minheap, [distance,points[i]])

        while k:
            res.append(heapq.heappop(minheap)[1])
            k-=1

        return res
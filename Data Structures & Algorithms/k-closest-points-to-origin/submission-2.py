import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distance = 0
        minheap = []
        for i in range(len(points)):

            distance = points[i][0]**2 + points[i][1]**2

            minheap.append([distance,points[i]])

        heapq.heapify(minheap)

        while k:
            res.append(heapq.heappop(minheap)[1])
            k-=1

        return res
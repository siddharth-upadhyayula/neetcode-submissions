class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        visited = [False]*n
        min_dist = [float("inf")]*n
        min_dist[0]=0
        total_cost = 0

        for _ in range(n):
            curr=-1

            for i in range(n):

                if not visited[i] and (curr==-1 or 
                min_dist[i]<min_dist[curr]):
                    curr=i

            
            visited[curr]=True        
            total_cost+=min_dist[curr]

            x1, y1 = points[curr]

            for neighbor in range(n):
                if not visited[neighbor]:
                    x2,y2 = points[neighbor]
                    distance = abs(x1-x2) + abs(y1-y2)

                    min_dist[neighbor] = min(min_dist[neighbor], distance)

        return total_cost

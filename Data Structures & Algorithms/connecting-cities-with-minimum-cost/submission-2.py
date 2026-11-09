class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        visited = [False]*(n+1)
        total_cost = 0
        minheap = [(0,1)]
        adj = [[] for i in range(n+1)]
        cities=0

        for a,b,cost in connections:
            adj[a].append((cost,b))
            adj[b].append((cost,a))



        while minheap:

            cost, city = heapq.heappop(minheap)

            if visited[city]:
                continue
            visited[city]=True
            total_cost+=cost
            cities+=1

            for c, neighbor in adj[city]:
                if not visited[neighbor]:
                    heapq.heappush(minheap, (c, neighbor))

        return total_cost if cities==n else -1
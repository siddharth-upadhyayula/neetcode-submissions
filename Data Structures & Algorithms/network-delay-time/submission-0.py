class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = collections.defaultdict(list)
        minheap = [(0, k)]
        for src, des, weight in times:
            adj[src].append([des, weight])

        visited = set()
        answer = 0


        while minheap:
            time, node = heapq.heappop(minheap)

            if node in visited:
                continue

            visited.add(node)
            answer = max(answer, time)

            for neighbor, w in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        minheap, 
                        (time+w, neighbor)
                    )

        return answer if len(visited)==n else -1
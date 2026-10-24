class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        hashmap = {}

        for i in range(len(tasks)):
            if tasks[i] in hashmap:
                hashmap[tasks[i]]-=1
            else:
                hashmap[tasks[i]]=-1

        for task, count in hashmap.items():
            heap.append((count, task))

        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1
            if heap:
                cnt, task = heapq.heappop(heap)
                cnt += 1
                if cnt != 0:
                    q.append((cnt, task, time + n))
            if q and q[0][2] == time:
                cnt, task, available_time = q.popleft()
                heapq.heappush(heap, (cnt, task))

        return time
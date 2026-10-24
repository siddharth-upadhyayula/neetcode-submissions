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
        cooldown_queue = deque()

        while heap or cooldown_queue:
            time+=1
            if heap:
                count, task = heapq.heappop(heap)
                count+=1
                if count!=0:
                    cooldown_queue.append((count, task, time+n))

            while cooldown_queue and cooldown_queue[0][2]==time:
                count,task,available_time = cooldown_queue.popleft()
                heapq.heappush(heap, (count,task))



        return time
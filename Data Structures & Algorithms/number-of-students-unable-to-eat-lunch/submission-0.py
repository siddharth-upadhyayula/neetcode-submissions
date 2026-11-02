class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        queue1 = deque(students)
        queue2 = deque(sandwiches)

        result = 0

        while queue1:
            if queue2[0] not in queue1:
                result += len(queue1)
                break
            if queue1[0] == queue2[0]:
                queue1.popleft()
                queue2.popleft()
            else:
                queue1.append(queue1.popleft())

        return result
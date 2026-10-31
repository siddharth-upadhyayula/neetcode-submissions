class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        indices = []  # stores indices

        for i, temp in enumerate(temperatures):
            while indices and temperatures[indices[-1]] < temp:
                prev_i = indices.pop()
                res[prev_i] = i - prev_i
            indices.append(i)

        return res

        Temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
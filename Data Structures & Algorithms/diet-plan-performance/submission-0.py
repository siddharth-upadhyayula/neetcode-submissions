class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0

        curr = sum(calories[:k])
        if curr < lower:
            score -= 1
        elif curr > upper:
            score += 1

        for i in range(k, len(calories)):
            curr += calories[i] - calories[i - k]
            if curr < lower:
                score -= 1
            elif curr > upper:
                score += 1

        return score
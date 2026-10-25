class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        max1 = max2 = max3 = 0
        for i in range(len(triplets)):
            curr1 = triplets[i][0]
            curr2 = triplets[i][1]
            curr3 = triplets[i][2]
            if curr1 <= target[0] and curr2 <= target[1] and curr3 <= target[2]:
                max1 = max(curr1, max1)
                max2 = max(curr2, max2)
                max3 = max(curr3, max3)

        return [max1, max2, max3] == target
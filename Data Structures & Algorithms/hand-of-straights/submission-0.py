class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for num in sorted(count):
            if count[num] > 0:
                frequency = count[num]

                for i in range(num, num + groupSize):
                    if count[i] < frequency:
                        return False

                    count[i] -= frequency

        return True
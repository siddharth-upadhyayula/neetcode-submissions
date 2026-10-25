class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize!=0:
            return False

        count = Counter(hand)

        for i in sorted(count):
            if count[i]>0:
                frequency = count[i]

                for j in range(i, groupSize+i):
                    if count[j]<frequency:
                        return False
                    count[j]-=frequency

        return True
                
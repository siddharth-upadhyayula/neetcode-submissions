class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        map = {5:0,10:0,20:0}

        for i in range(len(bills)):
            if bills[i]==5:
                map[bills[i]]+=1

            elif bills[i]==10:
                if map[5]<1:
                    return False
                map[5]-=1
                map[bills[i]]+=1

            elif bills[i]==20:
                if map[10]:
                    map[10]-=1
                    map[5]-=1
                else:
                    map[5]-=3

                if map[5]<0 or map[10]<0:
                    return False

        return True 

            

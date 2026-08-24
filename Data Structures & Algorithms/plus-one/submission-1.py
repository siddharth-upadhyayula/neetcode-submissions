class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = "".join(str(item) for item in digits)
        num = int(string)
        num+=1
        string = str(num)
        int_list = [int(x) for x in string]

        return int_list
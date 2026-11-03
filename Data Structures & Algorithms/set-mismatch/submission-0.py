class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(1,len(nums)+1):
            arr.append(i)

        result = []
        for val,freq in Counter(nums).items():
            if freq==2:
                result.append(val)

        for i in range(len(arr)):
            if arr[i] not in nums:
                result.append(arr[i])
        return result
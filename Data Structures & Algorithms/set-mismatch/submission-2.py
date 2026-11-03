class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:


        result = []
        for val,freq in Counter(nums).items():
            if freq==2:
                result.append(val)
        seen=set(nums)
        for i in range(1,len(nums)+1):
            if i not in seen:
                result.append(i)
        return result
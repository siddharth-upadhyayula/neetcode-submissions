class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []

        for i in range(len(nums1)):
            found = -1
            j = nums2.index(nums1[i])
            for k in range(j+1, len(nums2)): 
                if nums2[k]>nums2[j]:
                    found=nums2[k]
                    break
            res.append(found)


        return res
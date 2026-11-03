class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        result  =[]
        for i,val in enumerate(nums2):
            hashmap[val]=i

        for i in range(len(nums1)):
            result.append(hashmap[nums1[i]])

        return result
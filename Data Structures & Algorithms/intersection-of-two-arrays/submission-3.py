class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # result = set()

        # for i in range(min(len(nums1), len(nums2))):
        #     if nums1[i] in nums2:
        #         result.add(nums1[i])

        # return list(result)

        same = set(nums1) & set(nums2)

        return list(same)

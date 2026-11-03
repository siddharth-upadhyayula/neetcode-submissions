class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions = defaultdict(list)

        for j, value in enumerate(nums2):
            positions[value].append(j)

        mapping = []
        for value in nums1:
            mapping.append(positions[value].pop())
        return mapping
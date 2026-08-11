class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []

        for i in strs:
            key = "".join(sorted(i))
            if key in map:
                map[key].append(i)
            else:
                map[key]=[i]

        for i in map.values():
            res.append(i)

        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = defaultdict(set)
        nums = set(nums)
        seen = set()

        for n in nums:
            if n-1 not in nums:
                map[n].add(n)
                seen.add(n)

        while nums != seen:
            for n in nums:
                for key in map.keys():
                    if n-1 in map[key]:
                        map[key].add(n)
                        seen.add(n)

        max = 0
        for key in map.keys():
            if len(map[key]) > max:
                max = len(map[key])

        return max 
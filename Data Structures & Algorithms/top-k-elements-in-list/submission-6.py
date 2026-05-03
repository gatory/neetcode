class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            map[n] += 1

        for n, cnt in map.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            map[s[r]] += 1
            
            while ((r - l + 1) - max(map.values())) > k:
                map[s[l]] -= 1
                l += 1
            
            print(map)

            res = max(r - l + 1, res)
            
        return res
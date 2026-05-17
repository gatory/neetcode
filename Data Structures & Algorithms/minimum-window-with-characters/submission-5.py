class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        tCount = Counter(t)
        sCount = defaultdict(int)
        res = ""
        matches = 0

        l = 0
        for r in range(len(s)):
            if s[r] in tCount.keys():
                sCount[s[r]] += 1
                if sCount[s[r]] == tCount[s[r]]:
                    matches += 1

            if matches == len(tCount.keys()):
                while l <= r:
                    if s[l] in tCount.keys():
                        if res == "" or len(s[l:r+1]) < len(res):
                            res = s[l:r+1]
                         
                        sCount[s[l]] -= 1
                        if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                            matches -= 1
                            l += 1
                            break
                    l += 1
                    
        return res
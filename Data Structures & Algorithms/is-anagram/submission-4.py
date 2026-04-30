class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = dict()
        for c in s:
            if (c in map1.keys()):
                map1[c] += 1
            else:
                map1[c] = 0
        
        map2 = dict()
        for c in t:
            if (c in map2.keys()):
                map2[c] += 1
            else:
                map2[c] = 0
        
        return map1 == map2
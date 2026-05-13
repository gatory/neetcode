class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        for i, c in enumerate(s2):
            if c in s1 and Counter(s1) == Counter(s2[i:i+len(s1)]):
                return True


        return False
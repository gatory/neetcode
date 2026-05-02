class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= s
            res+= chr(0)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split(chr(0))
        res.pop()
        return res
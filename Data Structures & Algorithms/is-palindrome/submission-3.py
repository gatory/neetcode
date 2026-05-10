class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        s = "".join(char.lower() for char in s if char.isalpha() or char.isnumeric())
        print(s)

        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True
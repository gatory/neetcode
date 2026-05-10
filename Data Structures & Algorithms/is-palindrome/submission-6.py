class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        
        while start < end:
            # Skip non-alphanumeric from the left
            if not s[start].isalnum():
                start += 1
            # Skip non-alphanumeric from the right
            elif not s[end].isalnum():
                end -= 1
            # Compare
            else:
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
                
        return True
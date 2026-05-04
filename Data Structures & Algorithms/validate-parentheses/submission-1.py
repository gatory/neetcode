class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            
            if c in (')', '}', ']') and not stack:
                return False
            
            if c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            if c == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            if c == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False


        return bool(not stack)
                 
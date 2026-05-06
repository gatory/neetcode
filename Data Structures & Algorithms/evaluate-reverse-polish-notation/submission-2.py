class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in "+-*/":
                stack.append(int(s))
            else:
                b = stack.pop()
                a = stack.pop()
                if s == "+":
                    stack.append(a + b)
                elif s == "-":
                    stack.append(a-b)
                elif s == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[0]
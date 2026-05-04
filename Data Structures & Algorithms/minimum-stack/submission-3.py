class MinStack:

    def __init__(self):
        self.stack = []
        self.min = list()
        self.min.append(float('inf'))

    def push(self, val: int) -> None:
        if val <= self.min[-1]:
            self.min.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()

        if pop == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        

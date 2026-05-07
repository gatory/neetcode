class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = dict()

        for i, pos in enumerate(position):
            map[target - pos] = (target - pos) / speed[i]

        map = sorted(map.items())

        stack = []
        for distance, iterations in map:
            if stack and iterations <= stack[-1]:
                continue
            
            stack.append(iterations)

        return len(stack)
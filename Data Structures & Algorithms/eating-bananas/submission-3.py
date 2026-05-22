class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        best = high

        while low <= high:
            k = (low + high) // 2

            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p / k)

            if totalHours <= h:
                best = min(best, k)
                high = k - 1
            else:
                low = k + 1

        return best
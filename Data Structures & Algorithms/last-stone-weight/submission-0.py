class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            min1 = -heapq.heappop(maxHeap)
            min2 = -heapq.heappop(maxHeap)
            res = max(min1, min2) - min(min1, min2)

            print(res)
            if res > 0:
                heapq.heappush(maxHeap, -res)

        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
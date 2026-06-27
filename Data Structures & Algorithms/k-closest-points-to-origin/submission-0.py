class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(maxHeap, -dist)

            if len(maxHeap) > k:
                largest = heapq.heappop(maxHeap)

        res = []
        print(maxHeap)
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            if -dist in maxHeap:
                res.append(point)

        return res
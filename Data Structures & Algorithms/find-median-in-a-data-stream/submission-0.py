class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def addNum(self, num: int) -> None:
        if not self.rightHeap or num >= self.rightHeap[0]:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -num)

        while abs(len(self.leftHeap) - len(self.rightHeap)) > 1:
            if len(self.leftHeap) > len(self.rightHeap):
                popped = heapq.heappop(self.leftHeap)
                heapq.heappush(self.rightHeap, -popped)
            else:
                popped = heapq.heappop(self.rightHeap)
                heapq.heappush(self.leftHeap, -popped)
                
    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        elif len(self.leftHeap) < len(self.rightHeap):
            return self.rightHeap[0]
        else:
            return (self.rightHeap[0] - self.leftHeap[0]) / 2
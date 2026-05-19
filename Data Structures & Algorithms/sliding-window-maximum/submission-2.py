class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = list()
        maxHeap = list()
        heapq.heapify(maxHeap)
        
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
        
        res.append(-maxHeap[0])

        l = 0
        for r in range(k, len(nums)):
            heapq.heappush(maxHeap, -nums[r])
            maxHeap.remove(-nums[l])

            heapq.heapify(maxHeap)
            res.append(-maxHeap[0])
            
            l += 1

        
        

        return res
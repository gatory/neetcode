class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val -> index

        for index, num in enumerate(nums):
            lookup = target - num

            if lookup in prevMap:
                return [prevMap[lookup], index]
            
            prevMap[num] = index 
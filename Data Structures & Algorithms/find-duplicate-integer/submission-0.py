class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] << 1

        for num in nums:
            idx = num >> 1
            if nums[idx] & 1:
                return num >> 1
            
            else:
                nums[idx] = nums[idx] | 1

        return 0
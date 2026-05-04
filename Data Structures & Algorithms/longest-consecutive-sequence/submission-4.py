class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        heads = []

        max = 0
        for n in nums:
            if n-1 not in nums:
                length = 0
                counter = 0
                while n+counter in nums:
                    length += 1
                    counter += 1
                if length > max:
                    max = length

        return max
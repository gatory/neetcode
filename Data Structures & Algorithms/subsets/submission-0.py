class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(startIndex, current) -> None:
            result.append(list(current))
            
            for i in range(startIndex, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

            
        backtrack(0, [])

        return result
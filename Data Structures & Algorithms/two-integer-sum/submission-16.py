class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            c = target-n
            if c in d:
                return [d[c], i]
            d[n] = i        
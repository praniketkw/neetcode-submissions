class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.houserobber(nums[:-1]), self.houserobber(nums[1:]))
    
    def houserobber(self, arr):
        rob1,rob2 = 0,0

        for n in arr:
            tmp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2
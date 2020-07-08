class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            if i != 0:
                nums[i] = n + nums[i-1]
        return nums

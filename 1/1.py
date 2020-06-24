class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        b = enumerate(nums)
        for i, n in b:
            try:
                k = a[target - n]
                return i, k
            except:
                a[n] = i
            

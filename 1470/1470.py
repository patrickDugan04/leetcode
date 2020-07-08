class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        go = True
        left = 0
        right = 0
        b = []
        for i in range(2*n):
            if go:
                b.append(nums[left])
                left+=1
            else:
                b.append(nums[right + n])
                right+=1
            go = not go
        return b

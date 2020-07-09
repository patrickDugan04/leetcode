class Solution:
    def numberOfSteps (self, num: int) -> int:
        i = 0
        while True:
            if num == 0:
                return i
            elif num%2 == 0:
                num = num/2
                i+=1
            else:
                num -= 1
                i+=1

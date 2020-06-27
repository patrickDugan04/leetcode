class Solution:
    import math
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        a = (x<0)
        x = abs(x)
        b = int((str(x))[::-1])
        if math.log(b,2) > 31:
            return 0
        if a:
            b = b*-1
        return b

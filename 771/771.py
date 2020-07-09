class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        b = 0
        for i in J:
            b += S.count(i)
        return b

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        for i, n in enumerate(candies):
            out.append(max(candies) <= (n + extraCandies))
        return out

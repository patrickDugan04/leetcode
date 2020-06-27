class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = ''
        for g in digits:
          i+=str(g)
        i = str(int(i)+1)
        d = []
        for b in i:
            d.append(int(b))
        return d
            

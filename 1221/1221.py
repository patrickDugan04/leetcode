class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R = 0
        L = 0
        d = 0
        for i in s:
            if i == 'R':
                R+=1
            else:
                L+=1
            if R==L:
                d+=1
        return d
        

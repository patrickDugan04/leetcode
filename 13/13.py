def getval(a):
        if a == 'I':
            return 1
        elif a == 'V':
            return 5
        elif a == 'X':
            return 10
        elif a == 'L':
            return 50
        elif a == 'C':
            return 100
        elif a == 'D':
            return 500
        elif a == 'M':
            return 1000
        elif a == 'q':
            return 0
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s + "q"
        s = s[::-1]
        t = 0
        g = 0

        for i,b in enumerate(s):
            g = getval(b)
            if(g >= getval(s[i-1])):
                t += getval(b)
            else:
                t -= getval(b)
        return t

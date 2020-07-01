def remove(s):
    last = '!'
    l = []
    edit = False
    for i in s:
        if len(s) == 0:
            return "", False
        if i == last:
            l.pop()
            edit = True
            last = "!"
        else:
            l.append(i)
            last = i
    return l, edit
class Solution:
    def removeDuplicates(self, S: str) -> str:
        o = (S, True)
        while o[1]:
            o = remove(o[0])
        return "".join(o[0])

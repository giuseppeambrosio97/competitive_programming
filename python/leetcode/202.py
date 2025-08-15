class Solution:
    def isHappy(self, n: int) -> bool:
        V = set([n])
        tt = n
        while tt != 1:
            s = 0
            for ti in str(tt):
                s += int(ti)*int(ti)
            if s in V:
                return False
            V.add(s)
            tt = s
        return True


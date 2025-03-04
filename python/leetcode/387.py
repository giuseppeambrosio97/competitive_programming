from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()

        for i, si in enumerate(s):
            if si not in od:
                od[si] = (1,i)
            else:
                od[si] = (od[si][0]+1, od[si][1])

        for k,v in od.items():
            if v[0] == 1:
                return v[1]
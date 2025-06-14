class Solution:
    def minMaxDifference(self, num: int) -> int:
        ns = str(num)
        f = ns[0]
        i = 0
        while i < len(ns) and ns[i] == '9':
            i += 1
        max_ = int(ns.replace(ns[i])) if i < len(ns) else int(ns)
        min_ = int(ns.replace(f, "0"))
        return max_ - min_
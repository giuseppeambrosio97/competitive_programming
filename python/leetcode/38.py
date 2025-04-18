class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1) + "@"
        res = []
        l = 0
        for r in range(1,len(s)):
            if s[r] != s[r-1]:
                res.append(f"{(r-l)}{s[r-1]}")
                l = r
        return "".join(map(str,res))

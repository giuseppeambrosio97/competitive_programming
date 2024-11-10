
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        dm = {}
        im = {}

        for i in range(n):
            if s[i] in dm and dm[s[i]] != t[i]:
                return False
            if t[i] in im and im[t[i]] != s[i]:
                return False
            dm[s[i]] = t[i]
            im[t[i]] = s[i]
        return True



if __name__ == '__main__':
    s = "egg"
    t = "add"
    print(Solution().isIsomorphic(s,t))
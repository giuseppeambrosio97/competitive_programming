class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0

        for i in range(len(t)):
            if si < len(s) and t[i] == s[si]:
                si += 1

        return si == len(s)

if __name__ == '__main__':
    s = ""
    t = "ahbgdc"
    a = Solution().isSubsequence(s,t)
    print(a)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cval = int(s,2)
        slen = len(s)
        res = slen
        for i, si in enumerate(s):
            if cval <= k:
                return res
            if si == "1":
                cval -= 2**(slen-i-1)
                res -= 1
        return 0
    

if __name__ == "__main__":
    s = "1001010"
    k = 5
    print(Solution().longestSubsequence(s,k))
from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        VOCS = set("aeiou")

        cntr = Counter()
        maxv, maxc = 0, 0
        for si in s:
            cntr[si]+=1
            if si in VOCS:
                maxv = max(maxv, cntr[si])
            else:
                maxc = max(maxc, cntr[si])
        return maxv+maxc

if __name__ == "__main__":
    s = "successes"
    print(Solution().maxFreqSum(s))
from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        s += "@"
        l = 0
        m = defaultdict(int)
        for r in range(n):
            if s[r] != s[r + 1]:
                for t in range(1, r - l + 2):
                    m[s[l] * (t)] += r - l - t + 2
                l = r + 1
        max_ = -1
        for k, v in m.items():
            if v >= 3:
                max_ = max(max_, len(k))
        return max_


if __name__ == "__main__":
    s = "accbc"
    t = Solution().maximumLength(s)
    print(t)

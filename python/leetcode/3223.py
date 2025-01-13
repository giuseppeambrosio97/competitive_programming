from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)

        cnt = 0
        for c in counter.values():
            if c >= 3:
                cnt += c - (1 if c&1 else 2)
        return len(s) - cnt

if __name__ == '__main__':
    s = "abaacbcbb"
    print(Solution().minimumLength(s))
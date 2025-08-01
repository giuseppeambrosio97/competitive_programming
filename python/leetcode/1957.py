from collections import Counter


class Solution:
    def makeFancyString(self, s: str) -> str:
        # def fancy_check(i: int, ts: str) -> bool:
        #     """True the s[i] char can be added. False otherwise"""
        #     if i <= 1 or len(ts) <= 1:
        #         return True
        #     _most_common = Counter(ts[-2:]).most_common(1)[0]
        #     return _most_common[0] != s[i] or _most_common[1] < 2
        # ts = ""
        # for i, ch in enumerate(s):
        #     if fancy_check(i, ts):
        #         ts += ch
        # return ts
        prev = s[0]
        freq = 1
        res = ""

        for i in range(1, len(s)):
            if s[i] == prev:
                freq += 1
            else:
                freq = 1
                prev = s[i]
            if freq < 3:
                res += s[i]
        return res



if __name__ == "__main__":
    s = Solution().makeFancyString("leeetcode")
    print(s)

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """O(m*n)"""
        # cnt = 0
        # for w in words:
        #     nw, np = len(w), len(pref)
        #     if np <= nw:
        #         for i in range(np):
        #             if pref[i] != w[i]:
        #                 break
        #         if i == np-1 and pref[i] == w[i]:
        #             cnt += 1
        # return cnt
        """O(m*n)"""
        dct = {pref: 0}
        np = len(pref)
        for w in words:
            if w[:np] in dct:
                dct[pref] += 1
        return dct[pref]


if __name__ == '__main__':
    words = ["pay","attention","practice","attend"]
    pref = "at"
    t = Solution().prefixCount(words, pref)
    print(t)
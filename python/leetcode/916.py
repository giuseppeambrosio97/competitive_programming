from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # needed = defaultdict(int)

        # for w2 in words2:
        #     neededw2 = defaultdict(int)
        #     for w2i in w2:
        #         neededw2[w2i] += 1
        #         needed[w2i] = max(needed[w2i], neededw2[w2i])

        # res = []
        # for w1 in words1:
        #     w1counter = Counter(w1)
        #     good = True
        #     for letter, cnt in needed.items():
        #         if letter not in w1counter or cnt > w1counter[letter]:
        #             good = False
        #             break
        #     if good:
        #         res.append(w1)

        # return res
        """
        L1 = len(words1)
        L2 = len(words2)
        n2 = max(length w2)
        n1 = max(length w1)
        C = chs in needed

        T(n) = O(L2*n2 + L2*(n1+C))
        S(n) = O(C + n2)
        """

        needed = Counter()

        for w2 in words2:
            needed |= Counter(w2)

        return [w1 for w1 in words1 if not (needed - Counter(w1))]
    



if __name__ == '__main__':
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    t = Solution().wordSubsets(words1, words2)
    print(t)
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """O(n^2L)"""
        def is_prefix_and_suffix(w1: str, w2: str):
            n1, n2 = len(w1), len(w2)
            if n1 > n2:
                return False
            for i in range(n1):
                if w1[i] != w2[i] or w1[n1-i-1] != w2[n2-i-1]:
                    return False
            return True
        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if is_prefix_and_suffix(words[i], words[j]):
                    cnt += 1
        return cnt


if __name__ == '__main__':
    words = ["a","aba","ababa","aa"]
    t = Solution().countPrefixSuffixPairs(words)
    print(t)
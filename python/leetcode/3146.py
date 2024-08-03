class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        t_indexer = {ch: idx for idx, ch in enumerate(t)}
        sum_ = 0
        for idx, ch in enumerate(s):
            sum_ += abs(idx - t_indexer[ch])
        return sum_

if __name__ == '__main__':
    print(Solution().findPermutationDifference("abcde", "edbac"))
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """O(n^2*m^2)"""
        def is_substring(w1: str, w2: str):
            """n1*n2"""
            n1, n2 = len(w1), len(w2)
            if n1 <= n2:
                return False

            for i in range(n1):
                cnt = 0
                while i + cnt < n1 and cnt < n2 and w1[i + cnt] == w2[cnt]:
                    cnt += 1
                if cnt == n2:
                    return True

            return False

        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if is_substring(words[j], words[i]):
                    res.append(words[i])
                    break

        return res


if __name__ == "__main__":
    words = ["leetcoder","leetcode","od","hamlet","am"]
    r = Solution().stringMatching(words)
    print(r)

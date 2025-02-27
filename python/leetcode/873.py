from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        mapping = {a: idx for idx, a in enumerate(arr)}

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 2
                a, b = arr[i], arr[j]
                while a + b in mapping:
                    a, b = b, a + b
                    cnt += 1
                if cnt >= 3:
                    res = max(res, cnt)
        return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    Solution().lenLongestFibSubseq(arr)

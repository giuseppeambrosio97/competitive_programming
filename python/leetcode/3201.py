from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        best = -1
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            best = max(best, cnt)
        return best


if __name__ == "__main__":
    nums = [2, 39, 23]
    print(Solution().maximumLength(nums))

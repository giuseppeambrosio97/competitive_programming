from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)
        target = 0
        for n in nums:
            target |= n

        def count(idx: int, cor: int):
            if idx == N:
                return 1 if cor == target else 0
            return count(idx + 1, cor | nums[idx]) + count(idx + 1, cor)

        return count(0, 0)


if __name__ == "__main__":
    nums = [3, 2, 1, 5]
    print(Solution().countMaxOrSubsets(nums))

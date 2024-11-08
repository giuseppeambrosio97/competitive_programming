from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prefix_xor = [0 for _ in range(n)]

        for i, a in enumerate(nums):
            if i == 0:
                prefix_xor[-1] = a
            else:
                prefix_xor[n-i-1] = a ^ prefix_xor[n-i]

        res = []

        for p in prefix_xor:
            res.append(~p & ((1 << maximumBit) - 1))

        return res


if __name__ == '__main__':
    print(Solution().getMaximumXor([0,1,1,3], 2))
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        cnt0 = 0
        for n in nums:
            if n != 0:
                cnt0 = 0
            else:
                cnt0 += 1
                res += cnt0
        return res

if __name__ == "__main__":
    nums = [ 0, 0, 0, 2, 0, 0]
    print(Solution().zeroFilledSubarray(nums))

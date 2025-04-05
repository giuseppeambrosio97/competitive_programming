from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        res = [0]
        def back(idx: int, v: int = 0):
            res[0] += v
            for i in range(idx, N):
                back(i+1, v^nums[i])
        back(0)
        return res[0]



if __name__ == "__main__":
    nums = [5,1,6]
    print(Solution().subsetXORSum(nums))
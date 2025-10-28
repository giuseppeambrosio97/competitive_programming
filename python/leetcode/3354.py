from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # N = len(nums)
        # zeros = [i for i,a in enumerate(nums) if a == 0]
        # nonzero = N - len(zeros)
        # def check(i: int, d: int, nonzero: int) -> bool:
        #     # d=-1 left; d=1 right
        #     tmp = nums[::]
        #     while 0 <= i < N:
        #         if tmp[i] > 0:
        #             tmp[i] -= 1
        #             d *= -1
        #             if tmp[i] == 0:
        #                 nonzero -= 1
        #         i += d
        #     return nonzero == 0
        # res = 0
        # for i in zeros:
        #     if check(i,-1, nonzero):
        #         res += 1
        #     if check(i,1, nonzero):
        #         res += 1
        # return res
        res = 0
        L,R = 0,sum(nums)
        for a in nums:
            if a == 0:
                # check first left direction
                if 0 <= R - L <= 1:
                    res += 1
                # check right direction
                if 0 <= L - R <= 1:
                    res += 1
            else:
                L += a
                R -= a
        return res

if __name__ == "__main__":
    nums = [1,0,2,0,0]
    print(Solution().countValidSelections(nums))
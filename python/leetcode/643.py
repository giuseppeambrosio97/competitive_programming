from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cs = sum(nums[:k])
        best = cs
        l = 0
        r = k - 1
        while r < len(nums) - 1:
            cs = cs + nums[r + 1] - nums[l]
            best = max(cs, best)
            r += 1
            l += 1

        return best / k

        


if __name__ == '__main__':
    nums = [0,4,0,3,2]
    k = 1
    s = Solution().findMaxAverage(
        nums=nums,
        k=k,
    )
    print(s)
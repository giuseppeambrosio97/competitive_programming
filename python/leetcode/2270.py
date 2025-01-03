from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0]*(n+1)
        for i in range(1, n+1):
            psum[i] = psum[i-1] + nums[i-1]

        cnt = 0
        for i in range(1, n):
            if psum[i] >= psum[n] - psum[i]:
                cnt += 1
        return cnt

if __name__ == '__main__':
    nums = [10,4,-8,7]
    t = Solution().waysToSplitArray(nums)
    print(t)
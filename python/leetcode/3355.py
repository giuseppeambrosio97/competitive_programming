from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]*(n+1)
        for l,r in queries:
            diff[l] += 1
            diff[r+1] -= 1
        csum = 0
        for i in range(n):
            csum += diff[i]
            if csum < nums[i]:
                return False
        return True

if __name__ == "__main__":
    nums = [1,2,1,0,0,0]
    queries = [[0,2],[2,4]]
    print(Solution().isZeroArray(nums, queries))

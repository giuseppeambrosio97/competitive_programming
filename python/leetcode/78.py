from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, N = [], len(nums)
        def dfs(start, path: List[int]):
            res.append(path[:])
            for i in range(start,N):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))
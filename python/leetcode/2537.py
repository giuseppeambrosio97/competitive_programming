from typing import DefaultDict, List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = DefaultDict(int)
        n = len(nums)
        l = 0
        pair = 0
        res = 0
        for r in range(n):
            counter[nums[r]] += 1
            if counter[nums[r]] > 1:
                pair += counter[nums[r]] - 1
                while l < r and pair >= k:
                    res += (n-r)
                    if counter[nums[l]] > 1:
                        pair -= counter[l] + 1
                    counter[nums[l]] -= 1
                    l += 1
        return res
                

if __name__ == "__main__":
    nums = [3,1,4,3,2,2,4]
    k = 2
    print(Solution().countGood(nums, k))
            
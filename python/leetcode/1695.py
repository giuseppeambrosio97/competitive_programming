from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N, l = len(nums),0
        seen = set()
        res = 0
        csum = 0
        for r in range(N):
            while nums[r] in seen:
                seen.remove(nums[l])
                csum -= nums[l]
                l += 1
            seen.add(nums[r])
            csum += nums[r]
            res = max(res, csum)
        return res

if __name__ == "__main__":
    nums = [5,2,1,2,5,2,1,2,5]
    print(Solution().maximumUniqueSubarray(nums=nums))
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        csum = 0
        n = len(nums)
        fr = {}
        for i in range(k):
            csum += nums[i]
            if nums[i] not in fr:
                fr[nums[i]] = 0
            fr[nums[i]] += 1

        res = csum if len(fr) == k else 0
        
        l, r = 0, k
        while r < n:
            csum += nums[r]
            csum -= nums[l]
            if nums[r] not in fr:
                fr[nums[r]] = 0
            fr[nums[r]] += 1
            if fr[nums[l]] == 1:
                del fr[nums[l]]
            else:
                fr[nums[l]] -= 1
            if len(fr) == k:
                res = max(res, csum)
            r +=1
            l +=1
        return res


if __name__ == '__main__':
    nums = [4,4,4]
    k = 3
    s = Solution().maximumSubarraySum(nums, k)
    print(s)
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        l = 0
        nconsec = 1 # a sub array with one element have one consecutive element
        for r in range(n):
            if r > 0 and nums[r-1] + 1 == nums[r]:
                nconsec += 1

            if r - l + 1 > k:
                if nums[l] + 1 == nums[l+1]:
                    nconsec -= 1
                l += 1
            
            if r - l + 1 == k:
                res.append(nums[r] if nconsec == k else -1)
        
        return res


            

if __name__ == '__main__':
    nums = [1,2,3,4,3,2,3]
    k = 2
    a = Solution().resultsArray(nums, k)
    print(a)
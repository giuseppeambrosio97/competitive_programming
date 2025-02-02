from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        min_ = 101
        for x in nums:
            min_ = min(min_, x)
        
        for i, x in enumerate(nums):
            if x == min_:
                idx, max_, cnt = i, min_, 0
                while cnt < n-1:
                    next_ = (idx + 1) % n  
                    if nums[next_] < max_:
                        break
                    max_ = nums[next_]
                    cnt += 1
                    idx = next_
                if cnt == n - 1:
                    return True
        return False

if __name__ == '__main__':
    nums = [3,4,5,1,2]
    print(Solution().check(nums))
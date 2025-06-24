from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys_ids = [i for i, n in enumerate(nums) if n == key]
        res = []
        for kid in keys_ids:
            min_ = max(kid-k,0)
            up = min(kid+k,len(nums)-1)
            lb = min_ if not res or min_ > res[-1] else res[-1]+1
            res.extend(range(lb,up+1))
        return res
    
if __name__ == "__main__":
    nums = [3,4,9,1,3,9,5]
    key = 9
    k = 1 
    print(Solution().findKDistantIndices(nums, key, k))
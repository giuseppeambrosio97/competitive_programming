from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p)+1):
                pc = p.copy()
                pc.insert(i,nums[0])
                res.append(pc)
        
        return res
    
if __name__ == '__main__':
    nums = [1,0]
    t = Solution().permute(nums)
    print(t)
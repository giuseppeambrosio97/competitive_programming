from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def comb(combl: List, uset: Set):
            if len(uset) == 0:
                res.append(combl.copy())

            for n in uset:
                combl.append(n)
                use1 = uset.copy()
                use1.remove(n)
                comb(combl, use1)
                combl.pop()

        comb([], set(nums))
        return res
    
if __name__ == '__main__':
    nums = [1,0]
    t = Solution().permute(nums)
    print(t)
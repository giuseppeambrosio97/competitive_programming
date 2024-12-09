from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        l = 0
        n = len(nums)
        segs = []
        for r in range(n):
            if r > 0 and not (nums[r] & 1) ^ (nums[r-1] & 1):
                segs.append([l,r-1])
                l = r
        segs.append([l,r])
        ns = len(segs)

        def bs(query: List[int]) -> bool:
            l, r = 0, ns-1
            while l < r:
                m = l + ((r-l+1)//2)
                if segs[m][0] <= query[0]:
                    l = m
                else:
                    r = m - 1
            return segs[l][1] >= query[1]
        res = []
        for q in queries:
            res.append(bs(q))
        return res

if __name__ == '__main__':
    nums = [5,8,8,9]
    queries = [[1,2]]
    t = Solution().isArraySpecial(nums, queries)
    print(t)
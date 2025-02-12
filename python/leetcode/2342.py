from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def id_num(num: int) -> int:
            c = num
            sum_ = 0
            while c > 0:
                sum_ += c%10
                c //= 10
            return sum_

        m = defaultdict(list)
        
        res = -1
        for n in nums:
            idx = id_num(n)
            m[idx].append(n)
            if len(m[idx]) > 2:
                m[idx] = sorted(m[idx], reverse=True)[:2]
            if len(m[idx]) >= 2:
                res = max(res, sum(m[idx]))
        return res

        

if __name__ == "__main__":
    nums = [18,43,36,13,7]
    print(Solution().maximumSum(nums))
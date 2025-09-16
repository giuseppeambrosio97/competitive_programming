from functools import lru_cache
from typing import List
import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        @lru_cache(maxsize=None)
        def gcd(a,b):
            # a,b = max(a,b), min(a,b)
            # while b:
            #     a,b = b, a%b
            # return a
            return math.gcd(a,b)
        
        stack = []
        for n in nums:
            while stack and (g := gcd(n,stack[-1])) > 1:
                n = stack.pop()*n//g
            stack.append(n)
        return stack

if __name__ == "__main__":
    nums = [6,4,3,2,7,6,2]
    print(Solution().replaceNonCoprimes(nums))
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        note: psum[i] = a[0] + ... + a[i]
        sum(i,j) = psum[j] - psum[i-1]
        fr(t) = # p[j] s.t. p[j] = t

        cnt = 0
        for i in [0,..,n-1]:
            psum += nums[i]
            fr[psum] += 1
            if psum - k in fr:
                cnt += fr[psum-k]
        return cnt
        """
        cnt = 0
        n = len(nums)
        psum = 0
        fr = defaultdict(int)
        fr[0] = 1

        for i in range(n):
            psum += nums[i]
            cnt += fr[psum - k]
            fr[psum] += 1   

        return cnt
            

if __name__ == '__main__':

    nums = [1,1,-1]
    k = -1
    s = Solution().subarraySum(nums, k)
    print(s)
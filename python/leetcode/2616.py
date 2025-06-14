
class Solution:
    def minimizeMax(self, nums, p):
        if p == 0:
            return 0
        N = len(nums)
        nums.sort()

        
        def check(v: int) -> bool:
            cnt = 0
            i = 0
            while i < N-1 and cnt < p:
                if nums[i+1] - nums[i] <= v:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p


        l, r = 0, nums[-1] - nums[0]

        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return r


if __name__ == "__main__":
    nums = [3,4,2,3,2,1,2]
    p = 3
    print(Solution().minimizeMax(nums, p))
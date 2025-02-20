from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        T(n)=O(2^n)
        S(n)=O(n)
        """
        # n = len(nums)
        # nums = [int(n,2) for n in nums]

        # start = 0
        # for i in range(2**len(nums)):
        #     if i not in nums:
        #         start = i
        #         break
        # v = bin(start)[2:]
        # return "0"*(n-len(v)) + v
        
        M = set(nums)
        n = len(nums[0])

        def bk(p: List[str]):
            if len(p) == n:
                ps = "".join(map(str,p))
                if ps not in M:
                    return ps
                else:
                    return None
                
            for a in ["0", "1"]:
                p.append(a)

                r = bk(p)
                if r:
                    return r
                
                p.pop()

        return bk([])


if __name__ == "__main__":
    nums = ["01","10"]
    print(Solution().findDifferentBinaryString(nums))
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(choices: List[int], target: int, comb: List[int]):
            if target < 0:
                return
            if target == 0:
                res.append(comb.copy())

            for i,c in enumerate(choices):
                if c <= target:
                    comb.append(c)
                    bt(choices[i:], target-c, comb)
                    comb.pop()
        
        bt(candidates, target, [])

        return res

        
        

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    t = Solution().combinationSum(candidates, target)
    print(t)
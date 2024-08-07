from typing import List, Set
"""
class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        U = set(range(1,10))

        def _combinationSum3(S: Set[int], k: int, n: int) -> List[List[int]]:
            ""
            cs(S, k, n) = valid combinations such that:
                - exists in S k numbers that sum up to n

            recusive definition of the problem, you don't know which elements you can take so

            if |S| < k, n whatever -> nothing
            if k == 1 and in S exist a j s.t. j == n
                we have found a valid combination -> U / S 
            if k >= 2
                rs = []
                for each j in S
                    r = cs(S-{j}, k-1, n-j) # consider only the r s.t r is not None
                    rs.append(r)
                return rs
            return None 
            ""
            if len(S) < k or n < 0:
                return None
            
            if k == 1 and n in S:
                return list(U - S | {n})
            
            rs = []
            for i in S:
                r = _combinationSum3(S-{i}, k - 1, n - i)
                if r is not None and len(r) != 0:
                    rs.append(r)
            return rs
        
        return _combinationSum3(set(range(1,10)), k, n)
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def _combinationSum3(start: int, k: int, n: int) -> List[List[int]]:
            if k == 0 and n == 0:
                return [[]]
            if k < 0 or n < 0:
                return []
            
            results = []
            for i in range(start, 10):
                for combination in _combinationSum3(i + 1, k - 1, n - i):
                    results.append([i] + combination)
            return results
        
        return _combinationSum3(1, k, n)

if __name__ == '__main__':
    k = 2
    n = 5
    s = Solution().combinationSum3(k=k, n=n)
    print(s)
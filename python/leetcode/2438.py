from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        powers = []
        binn = bin(n)[2:][::-1]
        for i, b in enumerate(binn):
            bint = int(b)
            if bint:
                powers.append(1<<i)

        pprod = [1]*(len(powers)+1)
        for i in range(1, len(powers)+1):
            pprod[i] = (pprod[i-1]*powers[i-1]) % MOD

        res = []
        for l,r in queries:
            res.append(
                (pprod[r+1]*pow(pprod[l], MOD-2, MOD)) % MOD
            )

        return res


if __name__ == "__main__":
    n = 15
    queries = [[0,1],[2,2],[0,3]]    
    Solution().productQueries(n, queries)
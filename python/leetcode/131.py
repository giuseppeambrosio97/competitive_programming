from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        T(n)=O(N^2+N*2^N).
        S(n)=O(N^2) -> no output. O(N^2+N*2^N)
        """
        N = len(s)
        res = []

        # N^2
        dp = [[False]*N for _ in range(N)]
        for i in range(N-1,-1,-1):
            for j in range(i,N):
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True

        # O(N*2^N)
        def bk(start: int, parts: List[str]):
            if start >= N:
                res.append(parts[:])
                return
            
            for end in range(start,N): # find every j s.t. s[i]...s[j] is palidrome
                if not dp[start][end]:
                    continue
                parts.append(s[start:end+1])
                bk(end+1,parts)
                parts.pop()
        
        bk(0,[])
        return res

if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))
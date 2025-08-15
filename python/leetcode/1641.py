

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def dfs(s, l):
            if l == n:
                return 1
            res = 0
            for i in range(s,5):
                res += dfs(i,l+1)    
            return res    
       
        return dfs(0,0)

if __name__ == "__main__":
    n = 2
    print(Solution().countVowelStrings(n))
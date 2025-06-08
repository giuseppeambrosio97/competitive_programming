from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(curr: int):
            if curr > n:
                return
            res.append(curr)

            for i in range(10):
                next_ = curr*10 + i
                if next_ > n:
                    break
                dfs(next_)

        for i in range(1, 10):
            dfs(i)

        return res
        
        

if __name__ == "__main__":
    n = 13
    print(Solution().lexicalOrder(n))
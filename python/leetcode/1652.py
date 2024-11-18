from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0]*n
        
        if k > 0:
            r = []
            for i in range(n):
                s = 0
                for j in range(i+1, i+k+1):
                    s += code[j%n]
                r.append(s)
            return r
        
        r = []
        for i in range(n):
            s = 0
            for j in range(i-1, i+k-1,-1):
                s += code[j%n]
            r.append(s)
        return r

if __name__ == "__main__":
    code = [2,4,9,3]
    k = -2
    a = Solution().decrypt(code, k)
    print(a)
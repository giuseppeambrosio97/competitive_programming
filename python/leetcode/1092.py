
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Top down approach getting MLE
        T(n1,n2) = O(n1*n2*(n+m)) #n1+n2 for string concat
        S(n1,n2) = O(n1*n2*(n+m))
        """
        # n1, n2 = len(str1), len(str2)

        # @lru_cache(None)
        # def bk(i: int, j: int):
        #     if i == n1:
        #         return str2[j:]
        #     if j == n2:
        #         return str1[i:]

        #     if str1[i] == str2[j]:
        #         return str1[i] + bk(i + 1, j + 1)

        #     a = str1[i] + bk(i + 1, j)
        #     b = str2[j] + bk(i, j + 1)

        #     return a if len(a) < len(b) else b

        # return bk(0, 0)

        n1, n2 = len(str1), len(str2)
        prev = [str2[j:] for j in range(n2+1)]
        for i in range(n1-1, -1, -1):
            curr = [""] * n2
            curr.append(str1[i:])
            for j in range(n2-1, -1, -1):
                if str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j+1]
                else:
                    r1 = str1[i] + prev[j]
                    r2 = str2[j] + curr[j+1]
                    curr[j] = r1 if len(r1) < len(r2) else r2
            prev = curr

        return curr[0]
        
    



if __name__ == "__main__":
    str1 = "abac"
    str2 = "cab"
    Solution().shortestCommonSupersequence(str1, str2)

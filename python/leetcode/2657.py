from collections import defaultdict
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """T(n)=O(n)=S(n)"""
        # n = len(A)
        # mappingA, mappingB = {}, {}

        # for i in range(n):
        #     mappingA[A[i]] = i
        #     mappingB[B[i]] = i

        # res = [0]*n

        # for i in range(n):
        #     if i > 0:
        #         res[i]=res[i-1]
        #     if B[i] == A[i]:
        #         res[i]+= 1
        #     else:
        #         if i >= mappingA[B[i]]:
        #             res[i]+=1
        #         if i >= mappingB[A[i]]:
        #             res[i]+=1
        # return res
        """Cleaner approach T(n)=O(n)=S(n)."""
        # n = len(A)
        # seen = set()
        # counter = 0
        # res = []
        # for i in range(n):
        #     if A[i] in seen:
        #         counter += 1
        #     if B[i] in seen:
        #         counter += 1
        #     if A[i] == B[i]:
        #         counter += 1
        #     seen.add(A[i]), seen.add(B[i])
        #     res.append(counter)
        # return res 
        counter = defaultdict(int)
        n = len(A)
        res = [0]*n
        cnt = 0
        for i in range(n):
            counter[A[i]] += 1
            counter[B[i]] += 1
            if counter[A[i]] == 2:
                cnt += 1
            if counter[B[i]] == 2 and A[i] != B[i]:
                cnt += 1
            res[i] = cnt
        return res

if __name__ == '__main__':
    # A = [1,3,2,4]
    # B = [3,1,2,4]
    A = [2,3,1]
    B = [3,1,2]
    Solution().findThePrefixCommonArray(A, B)
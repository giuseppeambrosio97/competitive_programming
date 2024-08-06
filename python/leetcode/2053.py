from typing import List
from operator import itemgetter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        iterate over the arr: 
            use a dct: <key, value> <-> <arr[i], # of occurrences, first index occurrence>
        
        the solution is given by: 
            <arr[i], 1, j> j=0,..,k,..,n-1
            take the k element in that list sorted by j
        """
        import collections as cll
        aa = cll.Counter(arr)

        for a in aa.elements():
            print(a)
        return

        dct = {}
        for i, a in enumerate(arr):
            if a not in dct:
                dct[a] = (1, i)
            else:
                dct[a] = (dct[a][0] + 1, -1)

        distincts = [(key, times, index) for key, (times, index) in dct.items() if times == 1]

        distincts_sorted = sorted(distincts, key=itemgetter(2))

        return distincts_sorted[k-1][0] if len(distincts_sorted) >= k else ""

if __name__ == '__main__':
    arr, k = ["aaa","aa","a"], 4
    s = Solution().kthDistinct(arr, k)
    print(s)
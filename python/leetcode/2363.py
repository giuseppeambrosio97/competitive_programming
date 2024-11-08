from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dct = {}
        for a in items1+items2:
            if a[0] not in dct:
                dct[a[0]] = a[1]
            else:
                dct[a[0]] += a[1]

        return sorted([[v,w] for v,w in dct.items()], key=lambda x: x[0])


if __name__ == '__main__':
    items1 = [[1,1],[4,5],[3,8]]
    items2 = [[3,1],[1,5]]

    s = Solution().mergeSimilarItems(items1, items2)

    print(s)
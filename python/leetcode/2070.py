from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key=lambda x: x[0])
        maxs = [None] * len(items)
        max_ = - 1
        for i, itemi in enumerate(items):
            max_ = max(max_, itemi[1])
            maxs[i] = max_

        def query(query: int) -> int:            
            l, r = 0, len(items) - 1
            while l<r:
                m = (r + l) // 2 + 1
                
                if items[m][0] <= query and (m >= len(items) -1 or items[m+1][0] > query): 
                    return m

                if items[m][0] <= query:
                    l = m + 1
                else:
                    r = m - 1
            return r if items[r][0] <= query else -1
        res = []
        for q in queries:
            r = query(q)
            if r == -1:
                res.append(0)
            else:
                res.append(maxs[r])
        return res


if __name__ == '__main__':

    items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
    queries = [1,2,3,4,5,6]
    s = Solution().maximumBeauty(items, queries)
    print(s)
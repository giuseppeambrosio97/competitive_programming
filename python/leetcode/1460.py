from typing import List
import collections as cll

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return cll.Counter(target) == cll.Counter(arr)

if __name__ == '__main__':
    print(Solution().canBeEqual([1,2,2,3], [1,1,2,3]))
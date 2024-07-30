import collections
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct_frequency = collections.Counter(arr).values()
        return len(dct_frequency) == len(set(dct_frequency))
    

if __name__ == '__main__':
    print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
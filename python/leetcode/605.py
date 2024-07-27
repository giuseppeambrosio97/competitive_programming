from typing import List

class Solution:

    @staticmethod
    def _is_platable(flowerbed: List[int], idx: int) -> bool:

        if flowerbed[idx] == 1:
            return False
        
        _n = len(flowerbed)

        left = max(idx - 1, 0)
        right = min(idx + 1, _n - 1)

        return flowerbed[left] == 0 and flowerbed[right] == 0
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n > 0 and i < len(flowerbed):
            if Solution._is_platable(flowerbed, i):
                n -= 1
                i += 1
            i += 1

        return n == 0



if __name__ == '__main__':
    s = Solution()
    ss = s.canPlaceFlowers([1,0,0,0,0], 2)
    print(ss)
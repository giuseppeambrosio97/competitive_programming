from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for f in fruits:
            unset = 1
            for i, b in enumerate(baskets):
                if f <= b:
                    baskets[i] = 0
                    unset = 0
                    break
            count += unset
        return count


if __name__ == "__main__":
    fruits = [4,2,5]
    baskets = [3,5,4]
    print(Solution().numOfUnplacedFruits(fruits, baskets))
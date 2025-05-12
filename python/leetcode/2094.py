from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        res = set()

        def backtrack(path: List[int], curr_count: Counter):
            if len(path) == 3:
                if path[0] != 0 and path[2] % 2 == 0:
                    num = path[0] * 100 + path[1] * 10 + path[2]
                    res.add(num)
                return

            for digit in count:
                if curr_count[digit] < count[digit]:
                    path.append(digit)
                    curr_count[digit] += 1
                    backtrack(path, curr_count)
                    path.pop()
                    curr_count[digit] -= 1

        backtrack([], Counter())
        return sorted(res)


if __name__ == "__main__":
    print(Solution().findEvenNumbers([2,1,3,0]))
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res

if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))
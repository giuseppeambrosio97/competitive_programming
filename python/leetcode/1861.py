from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        # stone
        . empty
        * obstacle
        """
        m, n = len(box), len(box[0])
        def mv(row: List[str]):
            l, r = len(row) - 1, len(row) - 1

            while r >= 0:
                if row[r] == ".":
                    r-=1
                elif row[r] == "#":
                    row[l], row[r] = row[r], row[l]
                    r -= 1
                    l -= 1
                elif row[r] == "*":
                    r -= 1
                    l = r
            return row

        res = [["."] * m for _ in range(n)]
        for i, ri in enumerate(reversed(box)):
            newri = mv(ri)
            for j,a in enumerate(newri):
                res[j][i] = a

        return res


if __name__ == "__main__":
    box = [
        ["#", ".", "*", "."], 
        ["#", "#", "*", "."]
    ]
    s = Solution().rotateTheBox(box)
    print(s)

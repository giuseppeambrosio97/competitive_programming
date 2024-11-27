import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        nc = #cols = ceil(n/2numRows-2)
        S(n)=O(numRows*nc))=T(n)
        """
        # table = []
        # i, n = 0, len(s)
        # while i < n:
        #     col = [""] * numRows
        #     r = 0
        #     while i < n and r < numRows:
        #         col[r] = s[i]
        #         i += 1
        #         r += 1
        #     table.append(col)
        #     r = numRows - 2
        #     while i < n and r > 0:
        #         col = [""] * numRows
        #         col[r] = s[i]
        #         table.append(col)
        #         r -= 1
        #         i += 1
        # res = ""
        # for i in range(len(table[0])):
        #     for j in range(len(table)):
        #         if table[j][i] != "":
        #             res += table[j][i]
        # return res
        """T(n)=O(len(s))."""
        nr, n = numRows, len(s)
        if nr == 1:
            return s
        step = 2 * (nr - 1)
        res = ""
        for i in range(nr):
            for j in range(i, n, step):
                res += s[j]
                if i > 0 and i < nr - 1 and j + step - 2 * i < n:
                    res += s[j + step - 2 * i]
        return res

if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 1
    a = Solution().convert(s, numRows)
    print(a)

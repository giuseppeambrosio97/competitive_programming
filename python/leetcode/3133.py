class Solution:
    def minEnd(self, n: int, x: int) -> int:
        r = ""
        binx = bin(x)[2:][::-1]
        binn = bin(n-1)[2:][::-1]

        ix_, in_ = 0, 0

        while ix_ < len(binx) or in_ < len(binn):
            if ix_ > len(binx) - 1:
                r = f"{binn[in_]}{r}"
                in_ += 1
            elif binx[ix_] == "1":
                r = f"1{r}"
                ix_ += 1
            elif in_ > len(binn) - 1:
                r = f"0{r}"
                ix_ +=1
            else:
                r = f"{binn[in_]}{r}"
                in_ += 1
                ix_ += 1

        return int(r, 2)


if __name__ == "__main__":
    n = 1
    x = 4
    s = Solution().minEnd(n, x)
    print(s)

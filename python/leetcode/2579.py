class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        w = 2*n -1
        return w*w - 2*(n-1)*n

if __name__ == "__main__":
    n = 2
    print(Solution().coloredCells(n))
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        res = -1
        resstr = ""
        for r in range(len(num)):
            if num[r] != num[l]:
                l = r
            if r - l + 1 == 3:
                a = int(num[l:r+1])
                if res < a:
                    res = a
                    resstr = num[l:r+1]
                l = r + 1
        return resstr


if __name__ == "__main__":
    num = "6777133339"
    print(Solution().largestGoodInteger(num))
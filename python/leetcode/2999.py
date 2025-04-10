class Solution:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    ) -> int:
        start_ = str(start - 1)
        finish_ = str(finish)
        return self.F(finish_, s, limit) - self.F(start_, s, limit)

    def F(self, x: str, s: str, limit: int) -> int:
        if len(x) < len(s):
            return 0
        if len(x) == len(s):
            return 1 if x >= s else 0

        suffix = x[len(x)-len(s):]
        count = 0
        pre_len = len(x) - len(s)

        for i in range(pre_len):
            if limit < int(x[i]):
                count += (limit + 1) ** (pre_len - i)
                return count
            count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

        if suffix >= s:
            count += 1

        return count


if __name__ == "__main__":
    start = 1
    finish = 971
    limit = 9
    s = "72"
    print(Solution().numberOfPowerfulInt(start, finish, limit, s))
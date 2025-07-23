class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        targets = sorted([("ab", x), ("ba", y)], key=lambda t: -t[1])
        res = 0
        for t,r in targets:
            stack = []
            for i in range(len(s)):
                if stack and s[i] == t[1] and stack[-1] == t[0]:
                    stack.pop()
                    res += r
                else:
                    stack.append(s[i])
            s = stack
        return res


if __name__ == "__main__":
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    print(Solution().maximumGain(s,x,y))
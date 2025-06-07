from collections import Counter, deque


class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        res = []
        q = deque()
        min_ch = "a"
        for si in s:
            q.append(si)
            count[si] -= 1
            while min_ch != "z" and count[min_ch] == 0:
                min_ch = chr(ord(min_ch)+1)
            while q and q[-1] <= min_ch:
                res.append(q.pop())
        return "".join(res)

if __name__ == "__main__":
    s = "bdda"
    print(Solution().robotWithString(s))
from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque(s)

        q = deque()
        res = ""
        partial = ""
        while stack:
            ch = stack.pop()
            q.append(ch)
            if ch == "[":
                partial = q.pop()
                if partial == "[":
                    partial = ""
                times = ""
                while stack:
                    digit_ = stack.pop()
                    if not digit_.isnumeric():
                        stack.append(digit_)
                        break
                    times = f"{digit_}{times}"
                    
                while q:
                    chp = q.pop()
                    if chp == "]":
                        break
                    partial = f"{partial}{chp}"
                partial *= int(times)
                if len(q) != 0:
                    q.append(partial)
                else:
                   res = f"{partial}{res}"
            elif len(q) == 1 and ch.isalpha():
                q.pop()
                res = f"{ch}{res}"
        return res


if __name__ == '__main__':
    s = "10[b]"
    r = Solution().decodeString(s)
    print(r)
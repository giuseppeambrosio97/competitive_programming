class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for si in s:
            if si in dct:
                stack.append(dct[si])
            else:
                if not stack or stack[-1] != si:
                    return False
                stack.pop()
        return len(stack) == 0

if __name__ == "__main__":
    s = "()[]{}"
    res = Solution().isValid(s)
    print(res)
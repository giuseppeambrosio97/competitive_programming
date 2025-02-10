class Solution:
    def clearDigits(self, s: str) -> str:
        def is_non_digit(ch: str):
            return ord("a") <= ord(ch) <= ord("z")

        stack = []
        for ch in s:
            if is_non_digit(ch):
                stack.append(ch)
            else:
                stack.pop()
        
        return "".join(stack)
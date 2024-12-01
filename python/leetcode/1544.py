class Solution:
    def makeGood(self, s: str) -> str:
        def no_good(a,b):
            return abs(ord(a)-ord(b)) == 32
        
        i = 0
        stack = []
        n = len(s)

        while i < n:
            stack.pop() if stack and no_good(s[i], stack[-1]) else stack.append(s[i])

            i += 1

        return "".join(stack)





if __name__ == '__main__':
    s = "s"
    t = Solution().makeGood(s)
    print(t)
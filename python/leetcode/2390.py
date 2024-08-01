import collections as cll

class Solution:
    def removeStars(self, s: str) -> str:
        """
        Solution with no stack used
        def removeStars(self, s: str) -> str:
            i = len(s) - 1
            s_after = ""
            counter = 0
            while i >= 0:
                if s[i] == "*":
                    counter += 1
                else:
                    if counter > 0:
                        counter -= 1
                    else:
                        s_after = f"{s[i]}{s_after}" 
                
                i -= 1

            return s_after

        T(n) = O(n)
        S(n) = O(n)
        """
        stack = cll.deque()
        s_after = ""

        for i in range(len(s)):
            if s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])

        while stack:
            ch = stack.pop()
            s_after = f"{ch}{s_after}"

        return s_after


if __name__ == '__main__':
    print(Solution().removeStars("leet**cod*e"))

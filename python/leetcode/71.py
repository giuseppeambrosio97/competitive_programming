
class Solution:
    def simplifyPath(self, path: str) -> str:
        # parts = deque(path.split('/'))
        
        # simple = []
        # for p in parts:
        #     if p != "." and p != ".." and p != "":
        #         simple.append(p)
        #     elif p == ".." and simple:
        #         simple.pop()
        
        # return f"/{'/'.join(simple)}"
        s = []
        curr = ""

        for c in path + "/":
            if c == "/":
                if curr == ".." and s:
                    s.pop()
                elif curr != "." and curr != ".." and curr != "":
                    s.append(curr)
                curr = ""
            else:
                curr += c

        return "/" + "/".join(s)

if __name__ == '__main__':
    path = "/home/user/Documents//../Pictures"
    t = Solution().simplifyPath(path)
    print(t)
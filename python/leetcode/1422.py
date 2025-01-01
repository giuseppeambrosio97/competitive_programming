
class Solution:
    def maxScore(self, s: str) -> int:
        """
        s = "011101"
        psum0 = 0 1 1 1 1 2 2
        psum1 = 4 4 3 2 1 1 0       
        S(n)=O(n)=T(n)
        """
        # n = len(s)
        # psum0 = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     psum0[i] = psum0[i - 1] + (1 if s[i - 1] == "0" else 0)
        # psum1 = [0] * (n + 1)
        # for i in range(n-1, -1, -1):
        #     psum1[i] = psum1[i + 1] + (1 if s[i] == "1" else 0)
        # r = -1
        # for i in range(1, n):
        #     r = max(r, psum1[i]+psum0[i])
        # return r
        n = len(s)
        cnt0 = 0
        left1 = s.count("1")
        m = -1

        for i in range(n-1):
            if s[i] == "0":
                cnt0 += 1
            else:
                left1 -= 1
            m = max(m, cnt0+left1)
        return m


if __name__ == "__main__":
    s = "1111"
    t = Solution().maxScore(s)
    print(t)

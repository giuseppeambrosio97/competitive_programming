import re 

class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = re.split(r'\s+', s)
        splitted.reverse()
        return (" ".join(splitted)).strip()


if __name__ == '__main__':
    s = Solution()

    out = s.reverseWords("a good   example")

    print(out)
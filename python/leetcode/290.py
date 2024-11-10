class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False
        

        dm, im = {}, {}

        for pi, wi in zip(pattern, words):
            if pi in dm and dm[pi] != wi:
                return False
            
            if wi in im and im[wi] != pi:
                return False

            dm[pi] = wi
            im[wi] = pi

        return True

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    s = Solution().wordPattern(pattern, s)
    print(s)
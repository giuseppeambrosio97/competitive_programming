class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        i = 0
        cnt = 1
        while i < len(word):
            if i+1 < len(word) and cnt < 9 and word[i] == word[i+1]:
                cnt += 1
            else:
                comp += f"{cnt}{word[i]}"
                cnt = 1
            i += 1

        return comp



if __name__ == "__main__":
    a = Solution().compressedString("aaaaaaaaaab")
    print(a)
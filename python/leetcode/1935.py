class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(1 for t in text.split(" ") if not any(ch in broken for ch in t))

if __name__ == "__main__":
    text = "hello world"
    brokenLetters = "ad"
    print(Solution().canBeTypedWords(text,brokenLetters))

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 and any(c in word for c in "@#$"):
            return False
        
        
        word = word.lower()
        vowels = set("aeiou")

        has_voc = has_cons = False

        for w in word:
            if not w.isalpha():
                continue
            if w in vowels:
                has_voc = True
            else:
                has_cons = True

            if has_cons and has_voc:
                return True

        return has_cons and has_voc

if __name__ == "__main__":
    word = "234Adas"
    print(Solution().isValid(word))
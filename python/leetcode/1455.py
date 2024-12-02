class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # sentences = sentence.split(" ")
        # for i, s in enumerate(sentences):
        #     if len(s) >= len(searchWord):
        #         if s.startswith(searchWord):
        #             return i+1 
        # return -1

        l, r = 0, 0
        cnt = 0
        n = 1

        while l + len(searchWord) < len(sentence) and r < len(sentence):
            ## skip leading spaces
            if sentence[l] == " ":
                n += 1
            while sentence[l] == " ":
                l += 1
            ## compare
            r = l
            while r < len(sentence) and sentence[r] == searchWord[cnt]:
                cnt += 1
                if cnt >= len(searchWord):
                    return n
                r += 1
            while r < len(sentence) and sentence[r] != " ":
                r += 1
            cnt = 0
            l = r
        
        return -1

if __name__ == '__main__':
    sentence = "this problem is an easy problem"
    searchWord = "pro"
    t = Solution().isPrefixOfWord(sentence, searchWord)
    print(t)
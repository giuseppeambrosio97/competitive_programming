class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        for i in range(n):
            # n - numFriends + 1 is the max possible substring
            # in this way we find the longest at each index
            res = max(res, word[i:(i + n - numFriends + 1)])
        return res



if __name__ == "__main__":
    word = "dbca"
    numFriends = 2
    print(Solution().answerString(word, numFriends))

    
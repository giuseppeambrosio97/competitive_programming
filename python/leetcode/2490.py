class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        for curr, next in zip(words, words[1:] + words[:1]):
            if curr[-1] != next[0]:
                return False
            
        return True
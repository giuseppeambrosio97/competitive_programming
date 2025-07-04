from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0

        for i in range(len(words)):
            if length + len(line) + len(words[i]) > maxWidth:
                all_spaces = maxWidth - length
                spaces, remainder = divmod(all_spaces,max(1, len(line)-1))
                for j in range(max(1, len(line)-1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                
                res.append("".join(line))
                line, length = [], 0            
            line.append(words[i])
            length += len(words[i])
    
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space
        res.append(last_line)
        return res



if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    from pprint import pprint
    pprint(Solution().fullJustify(words, maxWidth))
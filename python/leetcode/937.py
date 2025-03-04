from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def log_key(l: str):
            idx, rest = l.split(" ", maxsplit=1)

            if rest[0].isdigit():
                return (1,)
            return (0, rest, idx)

        return sorted(logs, key=log_key)


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(Solution().reorderLogFiles(logs))
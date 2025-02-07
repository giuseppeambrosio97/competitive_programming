from collections import defaultdict
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        id_to_color = {}
        color_counter = defaultdict(int)
        unique_colors = 0

        for idx, color in queries:
            prev_color = id_to_color.get(idx)

            if prev_color == color:
                res.append(unique_colors)
                continue

            if prev_color is not None:
                color_counter[prev_color] -= 1
                if color_counter[prev_color] == 0:
                    unique_colors -= 1

            id_to_color[idx] = color
            color_counter[color] += 1
            if color_counter[color] == 1:
                unique_colors += 1

            res.append(unique_colors)

        return res

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            ## possible casees:
            # L...L -> fill L
            # R...R -> fill R
            # L...R -> skip forces in opposite direction
            # R...L -> balance the forces and one '.' if odd
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x == 'R' and y == 'L': 
                for k in range(i + 1, j):
                    if k - i == j - k:
                        ans[k] = '.'
                    elif k - i < j - k:
                        ans[k] = 'R'
                    else:
                        ans[k] = 'L'

        return "".join(ans)

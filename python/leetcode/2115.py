from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:  
        cancook = {s: True for s in supplies}
        recipe2idx = {r:idx for idx, r in enumerate(recipes)}

        def dfs(r: str) -> bool:
            if r in cancook:
                return cancook[r]
            if r not in recipe2idx:
                return False
            cancook[r] = False
            for nei in ingredients[recipe2idx[r]]:
                if not dfs(nei):
                    return False
            
            cancook[r] = True
            return True
        return [r for r in recipes if dfs(r)]
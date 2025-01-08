from typing import Dict


class Item:
    def __init__(self):
        self.end_item = False
        self.childs: Dict[str, Item] = {}


class WordDictionary:
    def __init__(self):
        self.root = Item()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.childs:
                curr.childs[w] = Item()
            curr = curr.childs[w]
        curr.end_item = True
        

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(item: Item, i: int):
            if i == n:
                return item.end_item
            
            if word[i] == ".":
                return any([dfs(a, i+1) for a in item.childs.values()])
            
            if word[i] not in item.childs:
                return False
            
            return dfs(item.childs[word[i]], i+1)
            
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
if __name__ == "__main__":
    obj = WordDictionary()
    word = "bad"
    obj.addWord(word)
    param_2 = obj.search("bbd")
    print(param_2)

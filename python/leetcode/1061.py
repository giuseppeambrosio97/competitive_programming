
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        get_id = lambda ch: ord(ch)-97
        
        edges = [set() for _ in range(26)]
        N = len(s1)
        for i in range(N):
            s1id = get_id(s1[i])
            s2id = get_id(s2[i])
            edges[s1id].add(s2id)
            edges[s2id].add(s1id)

        visited = set()
        comps = []
        def dfs(chid: int):
            visited.add(chid)
            res = set([chid])
            for nei in edges[chid]:
                if nei not in visited:
                    visited.add(nei)
                    res |= dfs(nei)

            return res

        for i in range(26):
            if i not in visited:
                dd = dfs(i)
                if len(dd) > 1:
                    comps.append(dd)

        mapping = [-1]*26
        for compid, comp in enumerate(comps):
            min_comp = min(list(comp))
            for chid in comp:
                mapping[chid] = min_comp

        res = []
        for i in range(len(baseStr)):
            bsid = get_id(baseStr[i])
            res.append(chr(97+(mapping[bsid] if mapping[bsid]!=-1 else bsid)))

        return "".join(res)

if __name__ == "__main__":
    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    Solution().smallestEquivalentString(s1,s2,baseStr)
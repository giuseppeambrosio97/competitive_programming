class Solution:
    def closestMeetingNode(self, edges, start1, start2):
        def dfs(current, distance, edges):
            dist = [-1] * len(edges)
            while current != -1 and dist[current] == -1:
                dist[current] = distance
                distance += 1
                current = edges[current]
            return dist
        res_id, res_val, n = -1, len(edges), len(edges)
        dist1 = dfs(start1, 0, edges)
        dist2 = dfs(start2, 0, edges)
        for i in range(n):
            if dist1[i] >= 0 and dist2[i] >= 0:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < res_val:
                    res_val = max_dist
                    res_id = i
        return res_id
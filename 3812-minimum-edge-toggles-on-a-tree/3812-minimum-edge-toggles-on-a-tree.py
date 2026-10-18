class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        adj = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, i))
            adj[v].append((u, i))

        diff = [a != b for a, b in zip(start, target)]
        parent = [-1] * n
        order = [0]

        #build tree order
        for u in order:
            for v, idx in adj[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                order.append(v)

        ans = []
        edge_id = [-1] * n

        for i, (u, v) in enumerate(edges):
            if parent[v] == u:
                edge_id[v] = i
            elif parent[u] == v:
                edge_id[u] = i

        #fix mismatches bottom up

        for u in reversed(order[1:]):
            if diff[u]:
                ans.append(edge_id[u])
                diff[parent[u]] = not diff[parent[u]]

        return sorted(ans) if not diff[0] else [-1]
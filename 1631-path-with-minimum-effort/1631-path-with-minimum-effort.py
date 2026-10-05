import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        R, C = len(heights), len(heights[0])
        best = [[float('inf')] * C for _ in range(R)]
        best[0][0] = 0
        heap = [(0, 0, 0)]   #(effort, row, col)
        while heap:
            e, r, c = heapq.heappop(heap)
            if r == R - 1 and c == C - 1:
                return e
            if e > best[r][c]:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    ne = max(e, abs(heights[nr][nc] - heights[r][c]))
                    if ne < best[nr][nc]:
                        best[nr][nc] = ne
                        heapq.heappush(heap, (ne, nr, nc))
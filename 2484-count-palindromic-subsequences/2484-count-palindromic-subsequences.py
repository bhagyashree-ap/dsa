class Solution:
    def countPalindromes(self, s):
        
        M = 10**9 + 7
        n = len(s)
        d = [int(c) for c in s]

        # suf[i][a][b] = pairs (a first, b later) using indices >= i
        suf = [None] * (n + 2)
        cur = [[0] * 10 for _ in range(10)]
        cnt = [0] * 10
        suf[n] = [row[:] for row in cur]
        
        for i in range(n - 1, -1, -1):
            x = d[i]
            for b in range(10):
                cur[x][b] = (cur[x][b] + cnt[b]) % M
            cnt[x] += 1
            suf[i] = [row[:] for row in cur]

        # pre[a][b] = pairs (a first, b later) using indices < i
        pre = [[0] * 10 for _ in range(10)]
        cnt = [0] * 10
        ans = 0
        
        for i in range(n):
            x = d[i]
            
            # i is the middle: left pair (a,b), right pair (b,a)
            for a in range(10):
                for b in range(10):
                    ans = (ans + pre[a][b] * suf[i + 1][b][a]) % M
            
            for a in range(10):
                pre[a][x] = (pre[a][x] + cnt[a]) % M
            cnt[x] += 1
        
        return ans
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])

        if k>=m+n-2:      #direct path
            return m+n-2

        q=deque([(0,0,k,0)])      #(row,col,kleft,steps)
        visit={(0,0,k)}
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r,c,rem,steps=q.popleft()

            if r==m-1 and c==n-1:
                return steps

            for drow,dcol in directions:
                newrow,newcol=r+drow,c+dcol

                if 0<=newrow<m and 0<=newcol<n:
                    newk=rem-grid[newrow][newcol]      #remaining k

                    if newk>=0 and (newrow,newcol,newk) not in visit:
                        visit.add((newrow,newcol,newk))
                        q.append((newrow,newcol,newk,steps+1))

        return -1
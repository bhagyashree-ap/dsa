class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols=len(grid), len(grid[0])
        visited=set()

        def dfs(r,c):
            #stop if invalid or already visited
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=='0' or (r,c) in visited):
                return
            
            visited.add((r,c))  #mark visited

            #visit neighbors
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        islands=0

        #check every cell
        for r in range(rows):
            for c in range(cols):
                
                #new island found
                if grid[r][c]=='1' and (r,c) not in visited:
                    islands+=1
                    dfs(r,c)
        
        return islands
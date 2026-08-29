class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]  #result
        path=[]   #current

        def bt(start):
            if len(path)==k:
                res.append(path[:])  #save
                return
            
            for i in range (start, n+1):
                path.append(i)  #add
                bt(i+1)   #recurse
                path.pop()  #undo
        
        bt(1)
        return res
            

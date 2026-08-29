class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t={}  #first table
        t_s={}  #second table

        for i in range (len(s)):
            x=s[i]
            y=t[i]

            if x in s_t and s_t[x] != y:
                return False    #check
            
            if y in t_s and t_s[y] != x:
                return False    #same value
            
            s_t[x]=y
            t_s[y]=x
        
        return True
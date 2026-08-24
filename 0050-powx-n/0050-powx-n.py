class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #negative power
        if n<0:
            x=1/x
            n=-n
        
        res=1.0

        while n>0:
            if n%2 == 1:    #odd exponent
                res*=x
        
            x *= x
            n //= 2     #half exponent

        return res
class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()

        while n!=1 and n not in seen:
            seen.add(n)  #mark seen

            total=0
            
            while n:
                digit=n%10    #last digit
                total+=digit*digit    #add square
                n//=10      #drop digit

            n=total  #next no.

        return n==1
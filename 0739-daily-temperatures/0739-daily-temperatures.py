class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n=len(temperatures)
        ans=[0]*n
        stack=[]

        #check each day
        for i in range(n):      
            
            #current day is warmer
            while stack and temperatures[i]>temperatures[stack[-1]]:      
                prev=stack.pop()
                ans[prev]=i-prev

            #current day waits
            stack.append(i)     
            
        return ans
            

            

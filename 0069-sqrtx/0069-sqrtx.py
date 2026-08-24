class Solution:
    def mySqrt(self, x: int) -> int:
        left, right=0,x     #range
        ans=0

        while left<=right:
            mid=(left+right)//2

            if mid*mid<=x:  
                ans=mid
                left=mid+1      #go right
            
            else:
                right=mid-1     #go left

        return ans
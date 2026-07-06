class Solution:
    def trap(self, height: List[int]) -> int:

        #initialize
        left=0
        right=len(height)-1
        lmax=0
        rmax=0
        water=0

        while left<right:

            #leftside
            if height[left]<height[right]:
                
                if height[left]>=lmax:
                    lmax=height[left]        #update lmax if current bar is taller
                else:
                    water+=lmax-height[left]   #add trapped water
                
                left+=1

            #rightside
            else:

                if height[right]>=rmax:
                    rmax=height[right]        #update rmax if current bar is taller
                else:
                    water+=rmax-height[right]   #add trapped water
                
                right-=1
        
        return water

        
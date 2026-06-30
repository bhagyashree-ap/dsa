class Solution:
    def maxArea(self, height: List[int]) -> int:
        #initialize two ptrs
        left=0
        right=len(height)-1

        max_area=0

        while left < right:
            #calculate area
            area=min(height[left], height[right])*(right-left)
            
            max_area=max(max_area,area)

            #move the shorter wall to find a taller one
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return max_area

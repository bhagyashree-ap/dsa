class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums.sort()   #sort elements
        
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:    #skip fixed element duplicates
                continue
            
            left=i+1   #set left ptr
            right=len(nums)-1    #set right ptr
            
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]   #calculate the threesum
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])  #append result
                    
                    while left<right and nums[left]==nums[left+1]:   #skip left duplicates
                        left+=1
                    
                    while left<right and nums[right]==nums[right-1]:   #skip right duplicates
                        right-=1
                    
                    left+=1
                    right-=1
                    
                elif current_sum < 0:
                    left+=1
                    
                else:
                    right-=1
        
        return result
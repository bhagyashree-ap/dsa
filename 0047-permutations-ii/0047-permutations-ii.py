class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        nums.sort()

        def bt(path, vis):
            
            if len(path)==len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if vis[i]:
                    continue
                
                #skip duplicate nos. at same level
                if i>0 and nums[i]==nums[i-1] and not vis[i-1]:
                    continue

                path.append(nums[i])
                vis[i]=True     #mark
                
                bt(path, vis)   #continue

                vis[i]=False    #unmark
                path.pop()
        
        bt([], [False]*len(nums))   #recursive backtracking

        return result
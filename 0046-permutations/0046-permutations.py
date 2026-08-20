class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def bt(path):
            if len(nums)==len(path):
                result.append(path[:])
                return

            for i in range (len(nums)): 
                if nums[i] not in path:
                    path.append(nums[i])    #add
                    bt(path)    #continue
                    path.pop()   #undo

        bt([])

        return result



        

        

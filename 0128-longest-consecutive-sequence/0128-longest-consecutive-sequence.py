class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)  #list->set
        longest=0

        for n in nums_set:
            #start of sequence
            if n-1 not in nums_set:
                length=1
                current_num=n
                
                #count length of current consecutive seq
                while current_num+1 in nums_set:   
                    current_num+=1
                    length+=1
                
                longest=max(longest,length)
        
        return longest
        
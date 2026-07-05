class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndex={}
        left=0
        longest=0

        for right in range(len(s)):

            #check duplicate in current window
            if s[right] in charIndex and charIndex[s[right]]>=left:
                left=charIndex[s[right]]+1    #skip duplicate
            
            charIndex[s[right]]=right

            longest=max(longest, right-left+1)
        
        return longest
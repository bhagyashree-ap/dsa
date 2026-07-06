class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #initalize two pointers
        left=0
        right=len(s)-1

        while left<right:

            #skip special chars from left
            if not s[left].isalnum():
                left+=1

            #skip special chars from right
            elif not s[right].isalnum():
                right-=1

            #chars don't match
            elif s[left].lower() != s[right].lower():
                return False
            
            #chars match, move both ptrs
            else:
                left+=1
                right-=1

        return True

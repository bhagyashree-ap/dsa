class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]
        pairs={'[':']', '{':'}', '(':')'}

        for char in s:
            
            if char in "{[(":   
                stack.append(char)
            
            else:               
                if not stack:      #no opening bracket
                    return False
                
                if pairs[stack[-1]]!=char:     #invalid pair
                    return False
                
                stack.pop()       
        
        return len(stack)==0      #all brackets matched

        
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return "" 

        rev=s[::-1]    #reverse string
        t=s+"#"+rev  #merge with separator

        lps=[0]*len(t) 
        j=0

        for i in range(1, len(t)):    #scan merged string
            while j>0 and t[i]!=t[j]:
                j=lps[j-1]    #backtrack with LPS

            if t[i]==t[j]:
                j+=1    #match found
                lps[i]=j    #save length

        longest=lps[-1]  #longest palindromic prefix

        return rev[:len(s)-longest]+s   #add missing chars in front
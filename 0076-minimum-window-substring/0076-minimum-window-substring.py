class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #edge case, for either empty string
        if not t or not s:
            return ""

        #initializing dictionaries
        count_t={}
        curr_window={}

        #count chars needed from t
        for i in t:
            count_t[i]=1+count_t.get(i,0)

        #sliding window
        already_have=0
        need=len(count_t)
        best_win=[-1, -1]
        win_len=float("inf")
        left=0

        #expand window
        for right in range(len(s)):
            i=s[right]
            curr_window[i]=1+curr_window.get(i,0)

            #req frequency reached
            if i in count_t and curr_window[i] == count_t[i]:
                already_have += 1
        
            while already_have == need:

                #update min window
                if (right-left+1)<win_len:
                    best_win=[left, right]
                    win_len=right-left+1
                
                #remove left char
                curr_window[s[left]]-=1

                #window does not satisfy req
                if s[left] in count_t and curr_window[s[left]] < count_t[s[left]]:
                    already_have -= 1
                left += 1
        
        #return ans
        left, right = best_win
        return s[left:right + 1] if win_len != float("inf") else ""




        
